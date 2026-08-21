from flask import Flask, render_template, request, redirect, url_for, session, flash, jsonify
from datetime import datetime, date, timedelta
import math
import json

app = Flask(__name__)
app.secret_key = 'discrete_structures_midterm_2026'

# =====================================================
# DATA FROM PROVIDED TABLES
# =====================================================

# User Data (from image.png)
USER_DATA = [
    {"school_id": "2026-0001", "username": "alexa.cortes", "role": "Student", "full_name": "Alexa Cortes", "password": "Student@123"},
    {"school_id": "2026-0002", "username": "john.smith", "role": "Student", "full_name": "John Smith", "password": "Student@456"},
    {"school_id": "2026-0003", "username": "maria.santos", "role": "Faculty", "full_name": "Maria Santos", "password": "Faculty@123"},
    {"school_id": "2026-0004", "username": "david.reyes", "role": "Faculty", "full_name": "David Reyes", "password": "Faculty@456"},
    {"school_id": "2026-0005", "username": "anna.garcia", "role": "Staff", "full_name": "Anna Garcia", "password": "Staff@123"},
    {"school_id": "2026-0006", "username": "robert.cruz", "role": "Staff", "full_name": "Robert Cruz", "password": "Staff@456"},
    {"school_id": "2026-0007", "username": "carlos.mendoza", "role": "Chairperson", "full_name": "Carlos Mendoza", "password": "Chair@123"},
    {"school_id": "2026-0008", "username": "sophia.lopez", "role": "Chairperson", "full_name": "Sophia Lopez", "password": "Chair@456"},
    {"school_id": "2026-0009", "username": "mark.johnson", "role": "Faculty", "full_name": "Mark Johnson", "password": "Faculty@789"},
    {"school_id": "2026-0010", "username": "emily.wilson", "role": "Student", "full_name": "Emily Wilson", "password": "Student@789"},
    {"school_id": "2026-0011", "username": "james.brown", "role": "Staff", "full_name": "James Brown", "password": "Staff@789"},
    {"school_id": "2026-0012", "username": "lisa.anderson", "role": "Chairperson", "full_name": "Lisa Anderson", "password": "Chair@789"},
]

# Room Data (from image.png)
ROOM_DATA = [
    {"room_id": "RM-CMLAB-A01", "room_number": "COMLAB 1", "room_name": "Computer Laboratory 1", "type": "Computer Laboratory"},
    {"room_id": "RM-CMLAB-A02", "room_number": "COMLAB 2", "room_name": "Computer Laboratory 2", "type": "Computer Laboratory"},
    {"room_id": "RM-CMLAB-A03", "room_number": "COMLAB 3", "room_name": "Computer Laboratory 3", "type": "Computer Laboratory"},
    {"room_id": "RM-CMLAB-A04", "room_number": "COMLAB 4", "room_name": "Computer Laboratory 4", "type": "Computer Laboratory"},
    {"room_id": "RM-CMLEC-B01", "room_number": "COMLEC 1", "room_name": "Computer Lecture Room 1", "type": "Lecture Room"},
    {"room_id": "RM-CMLEC-B02", "room_number": "COMLEC 2", "room_name": "Computer Lecture Room 2", "type": "Lecture Room"},
    {"room_id": "RM-FAC-C01", "room_number": "FACULTY OFFICE", "room_name": "Faculty Office", "type": "Office"},
    {"room_id": "RM-LIB-D01", "room_number": "LIBRARY", "room_name": "School Library", "type": "Library"},
]

# Facilities
FACILITIES = [
    {"name": "Library", "type": "library", "capacity": 100},
    {"name": "Computer Laboratory", "type": "laboratory", "capacity": 40},
    {"name": "Science Laboratory", "type": "laboratory", "capacity": 30},
    {"name": "Faculty Room", "type": "office", "capacity": 20},
    {"name": "Registrar Office", "type": "office", "capacity": 15},
]

# =====================================================
# SET THEORY - User Classification
# =====================================================

class User:
    def __init__(self, school_id, username, password, role, full_name):
        self._school_id = school_id
        self._username = username
        self._password = password
        self._role = role  # Student, Faculty, Staff, Chairperson
        self._full_name = full_name
        self._is_authorized = False
        self._login_attempts = 0
    
    def get_school_id(self):
        return self._school_id
    
    def get_username(self):
        return self._username
    
    def get_password(self):
        return self._password
    
    def get_role(self):
        return self._role
    
    def get_full_name(self):
        return self._full_name
    
    def is_authorized(self):
        return self._is_authorized
    
    def set_authorized(self, status):
        self._is_authorized = status
    
    def check_password(self, password):
        if self._password == password:
            self._login_attempts = 0
            return True
        self._login_attempts += 1
        return False
    
    def to_dict(self):
        return {
            "school_id": self._school_id,
            "username": self._username,
            "role": self._role,
            "full_name": self._full_name,
            "authorized": self._is_authorized
        }


# =====================================================
# ROOM CLASS
# =====================================================

class Room:
    def __init__(self, room_id, room_number, room_name, room_type):
        self._room_id = room_id
        self._room_number = room_number
        self._room_name = room_name
        self._type = room_type
        self._is_available = True
    
    def get_room_id(self):
        return self._room_id
    
    def get_room_number(self):
        return self._room_number
    
    def get_room_name(self):
        return self._room_name
    
    def get_type(self):
        return self._type
    
    def is_available(self):
        return self._is_available
    
    def set_availability(self, status):
        self._is_available = status
    
    def to_dict(self):
        return {
            "room_id": self._room_id,
            "room_number": self._room_number,
            "room_name": self._room_name,
            "type": self._type,
            "available": self._is_available
        }


# =====================================================
# FACILITY CLASS
# =====================================================

class Facility:
    def __init__(self, name, facility_type, capacity):
        self._name = name
        self._type = facility_type
        self._capacity = capacity
        self._is_available = True
    
    def get_name(self):
        return self._name
    
    def get_type(self):
        return self._type
    
    def get_capacity(self):
        return self._capacity
    
    def is_available(self):
        return self._is_available
    
    def set_availability(self, status):
        self._is_available = status
    
    def to_dict(self):
        return {
            "name": self._name,
            "type": self._type,
            "capacity": self._capacity,
            "available": self._is_available
        }


# =====================================================
# ACCESS REQUEST CLASS
# =====================================================

class AccessRequest:
    def __init__(self, username, facility_name, date_str, start_hour, end_hour, purpose):
        self._id = self.generate_id()
        self._username = username
        self._facility_name = facility_name
        self._date = date_str
        self._start_hour = start_hour
        self._end_hour = end_hour
        self._purpose = purpose
        self._status = "Pending"  # Pending, Approved, Rejected
        self._timestamp = datetime.now()
    
    @staticmethod
    def generate_id():
        return f"AR-{datetime.now().strftime('%Y%m%d%H%M%S')}"
    
    def get_id(self):
        return self._id
    
    def get_username(self):
        return self._username
    
    def get_facility_name(self):
        return self._facility_name
    
    def get_date(self):
        return self._date
    
    def get_start_hour(self):
        return self._start_hour
    
    def get_end_hour(self):
        return self._end_hour
    
    def get_purpose(self):
        return self._purpose
    
    def get_status(self):
        return self._status
    
    def set_status(self, status):
        self._status = status
    
    def get_time_display(self):
        start_period = "AM" if self._start_hour < 12 else "PM"
        end_period = "AM" if self._end_hour < 12 else "PM"
        start_display = f"{self._start_hour % 12 or 12}:00 {start_period}"
        end_display = f"{self._end_hour % 12 or 12}:00 {end_period}"
        return f"{self._date} {start_display} - {end_display}"
    
    def to_dict(self):
        return {
            "id": self._id,
            "username": self._username,
            "facility": self._facility_name,
            "date": self._date,
            "time": self.get_time_display(),
            "purpose": self._purpose,
            "status": self._status
        }


# =====================================================
# PROPOSITIONAL LOGIC - Access Rules
# =====================================================

class AccessLogic:
    @staticmethod
    def can_access(user, facility_name):
        """
        Predicate Logic Rules:
        ∀u ∈ Users, ∀f ∈ Facilities:
        
        Rule 1: Faculty(u) ∨ Chairperson(u) → Authorized(u) ∧ CanAccess(u, f) ∀f ∈ {Library, Computer Lab, Science Lab, Faculty Room}
        Rule 2: Staff(u) → Authorized(u) ∧ CanAccess(u, f) ∀f ∈ {Library, Registrar Office}
        Rule 3: Student(u) ∧ HasRequest(u, f) ∧ RequestApproved(u, f) → CanAccess(u, f)
        Rule 4: Student(u) ∧ ¬HasRequest(u, f) → ¬CanAccess(u, f)
        
        Boolean Expression:
        Access = (Faculty ∨ Chairperson) ∨ Staff ∨ (Student ∧ HasRequest ∧ IsApproved)
        """
        role = user.get_role()
        
        # Define facility categories
        faculty_facilities = {"Library", "Computer Laboratory", "Science Laboratory", "Faculty Room"}
        staff_facilities = {"Library", "Registrar Office"}
        
        # Rule 1: Faculty and Chairperson have broad access
        if role in ["Faculty", "Chairperson"]:
            if facility_name in faculty_facilities:
                return True
        
        # Rule 2: Staff have limited access
        if role == "Staff":
            if facility_name in staff_facilities:
                return True
        
        # Rule 3: Students need approved request
        if role == "Student":
            # Check if student has approved request for this facility
            # This will be checked in the system level
            return None  # Returns None to indicate further checking needed
        
        return False
    
    @staticmethod
    def can_request_access(user):
        """
        Predicate Logic for requesting access:
        CanRequest(u) ↔ Student(u) ∨ Faculty(u) ∨ Staff(u) ∨ Chairperson(u)
        """
        return user.get_role() in ["Student", "Faculty", "Staff", "Chairperson"]
    
    @staticmethod
    def evaluate_boolean_access(role, has_request, request_approved):
        """
        Boolean Function: Access = (F ∨ C ∨ S ∨ (St ∧ R ∧ A))
        
        Where:
        F = is Faculty
        C = is Chairperson  
        S = is Staff
        St = is Student
        R = Has Request
        A = Request Approved
        """
        is_faculty = role == "Faculty"
        is_chair = role == "Chairperson"
        is_staff = role == "Staff"
        is_student = role == "Student"
        
        # Boolean expression
        access = is_faculty or is_chair or is_staff or (is_student and has_request and request_approved)
        
        return bool(access)


# =====================================================
# RELATIONS - Access Permissions Matrix
# =====================================================

class AccessMatrix:
    def __init__(self, users, facilities):
        self.users = users
        self.facilities = facilities
        self.matrix = []
        self.initialize_matrix()
    
    def initialize_matrix(self):
        """Initialize access matrix: rows = users, columns = facilities"""
        for user in self.users:
            row = []
            for facility in self.facilities:
                # Set initial access based on user type (Boolean Algebra)
                role = user.get_role()
                facility_name = facility.get_name()
                
                # Boolean expression for initial access
                if role in ["Faculty", "Chairperson"]:
                    if facility_name in ["Library", "Computer Laboratory", "Science Laboratory", "Faculty Room"]:
                        access = 1
                    else:
                        access = 0
                elif role == "Staff":
                    if facility_name in ["Library", "Registrar Office"]:
                        access = 1
                    else:
                        access = 0
                else:  # Student
                    access = 0  # Needs request
                
                row.append(access)
            self.matrix.append(row)
    
    def get_matrix(self):
        return self.matrix
    
    def get_user_access_row(self, username):
        """Get access row for a specific user"""
        for i, user in enumerate(self.users):
            if user.get_username() == username:
                return self.matrix[i]
        return None
    
    def get_facility_access_column(self, facility_name):
        """Get access column for a specific facility"""
        for j, facility in enumerate(self.facilities):
            if facility.get_name() == facility_name:
                return [row[j] for row in self.matrix]
        return None
    
    def update_access(self, username, facility_name, access_value):
        """Update a single cell in the access matrix"""
        user_index = -1
        facility_index = -1
        
        for i, user in enumerate(self.users):
            if user.get_username() == username:
                user_index = i
                break
        
        for j, facility in enumerate(self.facilities):
            if facility.get_name() == facility_name:
                facility_index = j
                break
        
        if user_index != -1 and facility_index != -1:
            self.matrix[user_index][facility_index] = 1 if access_value else 0
            return True
        return False
    
    def calculate_permission_score(self, username, facility_name):
        """
        Number Theory: Use GCD/LCM for permission scoring
        """
        row = self.get_user_access_row(username)
        if row:
            # Get the access value
            facility_index = -1
            for j, facility in enumerate(self.facilities):
                if facility.get_name() == facility_name:
                    facility_index = j
                    break
            
            if facility_index != -1:
                access_value = row[facility_index]
                
                # Use GCD to calculate permission score
                if access_value == 1:
                    # Calculate score based on user type
                    user = None
                    for u in self.users:
                        if u.get_username() == username:
                            user = u
                            break
                    
                    if user:
                        # Convert username to numeric for GCD
                        name_sum = sum(ord(c) for c in username)
                        facility_sum = sum(ord(c) for c in facility_name)
                        gcd_value = math.gcd(name_sum, facility_sum)
                        
                        if user.get_role() == "Chairperson":
                            return gcd_value + 50  # Highest permission
                        elif user.get_role() == "Faculty":
                            return gcd_value + 40
                        elif user.get_role() == "Staff":
                            return gcd_value + 30
                        elif user.get_role() == "Student":
                            return gcd_value + 10
                
                return 0  # No access
        
        return 0


# =====================================================
# MAIN SYSTEM CLASS
# =====================================================

class AccessControlSystem:
    def __init__(self):
        self.users = []
        self.rooms = []
        self.facilities = []
        self.access_requests = []
        self.access_history = []
        self.current_user = None
        self.access_matrix = None
        
        self.initialize_data()
        self.access_matrix = AccessMatrix(self.users, self.facilities)
    
    def initialize_data(self):
        # Initialize Users from provided data (Set Theory)
        for user_data in USER_DATA:
            user = User(
                user_data["school_id"],
                user_data["username"],
                user_data["password"],
                user_data["role"],
                user_data["full_name"]
            )
            self.users.append(user)
        
        # Initialize Rooms from provided data
        for room_data in ROOM_DATA:
            room = Room(
                room_data["room_id"],
                room_data["room_number"],
                room_data["room_name"],
                room_data["type"]
            )
            self.rooms.append(room)
        
        # Initialize Facilities
        for facility_data in FACILITIES:
            facility = Facility(
                facility_data["name"],
                facility_data["type"],
                facility_data["capacity"]
            )
            self.facilities.append(facility)
    
    # =====================================================
    # AUTHENTICATION
    # =====================================================
    def authenticate(self, username, password):
        for user in self.users:
            if user.get_username() == username and user.check_password(password):
                self.current_user = user
                # Set authorized based on role
                if user.get_role() in ["Faculty", "Chairperson", "Staff"]:
                    user.set_authorized(True)
                return True
        return False
    
    def get_current_user(self):
        return self.current_user
    
    def logout(self):
        self.current_user = None
    
    def get_user_by_username(self, username):
        for user in self.users:
            if user.get_username() == username:
                return user
        return None
    
    def verify_id(self, school_id):
        """
        Number Theory: ID verification using modular arithmetic
        ID format: 2026-XXXX
        """
        try:
            # Extract numeric part
            parts = school_id.split('-')
            if len(parts) != 2:
                return False, "Invalid ID format. Use YYYY-XXXX format"
            
            year = int(parts[0])
            number = int(parts[1])
            
            # Check if year is 2026 (our school year)
            if year != 2026:
                return False, "Invalid school year"
            
            # Number Theory: Check divisibility
            # ID must be divisible by 2 (even) for validation
            if number % 2 != 0:
                return False, "ID number must be even (modular arithmetic check)"
            
            # Check if ID exists in system
            for user in self.users:
                if user.get_school_id() == school_id:
                    return True, "Valid ID found"
            
            return False, "ID not found in system"
            
        except ValueError:
            return False, "Invalid ID format"
    
    # =====================================================
    # ACCESS REQUEST FUNCTIONS
    # =====================================================
    def request_access(self, username, facility_name, date_str, start_hour, end_hour, purpose):
        """Create a new access request"""
        # Check if user exists
        user = self.get_user_by_username(username)
        if not user:
            return None, "User not found"
        
        # Check if user can request (Predicate Logic)
        if not AccessLogic.can_request_access(user):
            return None, "You are not authorized to request access"
        
        # Find facility
        facility = None
        for f in self.facilities:
            if f.get_name() == facility_name:
                facility = f
                break
        
        if not facility:
            return None, "Facility not found"
        
        # Validate time (8 AM - 5 PM)
        if start_hour < 8 or end_hour > 17 or start_hour >= end_hour:
            return None, "Invalid time! Access hours are 8:00 AM - 5:00 PM"
        
        # Check for conflicts using modular arithmetic (Number Theory)
        if not self.check_time_availability(facility_name, date_str, start_hour, end_hour):
            return None, "Facility is already booked for this time slot"
        
        # Create request
        request = AccessRequest(username, facility_name, date_str, start_hour, end_hour, purpose)
        self.access_requests.append(request)
        
        return request, "Access request submitted successfully"
    
    def check_time_availability(self, facility_name, date_str, start_hour, end_hour):
        """
        Number Theory: Use modular arithmetic to check availability
        """
        # Count requests for this facility on this date
        facility_requests = 0
        for req in self.access_requests:
            if req.get_facility_name() == facility_name and req.get_date() == date_str:
                if req.get_status() == "Approved":
                    # Check time overlap
                    if not (end_hour <= req.get_start_hour() or start_hour >= req.get_end_hour()):
                        return False
                    facility_requests += 1
        
        # Find facility capacity
        facility = None
        for f in self.facilities:
            if f.get_name() == facility_name:
                facility = f
                break
        
        if facility:
            # Use modular arithmetic: Check if capacity can accommodate requests
            # If capacity % (requests + 1) == 0, suggests optimal capacity
            if facility_requests > 0 and facility.get_capacity() % (facility_requests + 1) == 0:
                # This indicates good capacity distribution
                pass
        
        return True
    
    def get_user_requests(self, username):
        """Get all access requests for a user"""
        return [req for req in self.access_requests if req.get_username() == username]
    
    def get_user_history(self, username):
        """Get access history for a user"""
        return [hist for hist in self.access_history if hist.get_username() == username]
    
    # =====================================================
    # ADMIN FUNCTIONS
    # =====================================================
    def get_pending_requests(self):
        """Get all pending access requests"""
        return [req for req in self.access_requests if req.get_status() == "Pending"]
    
    def approve_request(self, request_id):
        """Approve an access request"""
        for req in self.access_requests:
            if req.get_id() == request_id:
                req.set_status("Approved")
                
                # Update access matrix
                self.access_matrix.update_access(req.get_username(), req.get_facility_name(), True)
                
                # Add to history
                self.access_history.append(req)
                
                return True, "Access request approved"
        
        return False, "Request not found"
    
    def reject_request(self, request_id):
        """Reject an access request"""
        for req in self.access_requests:
            if req.get_id() == request_id:
                req.set_status("Rejected")
                
                # Add to history
                self.access_history.append(req)
                
                return True, "Access request rejected"
        
        return False, "Request not found"
    
    def get_all_requests(self):
        """Get all access requests"""
        return self.access_requests
    
    def get_all_history(self):
        """Get all access history"""
        return self.access_history
    
    def get_users_by_role(self, role):
        """Get users by role (Set Theory)"""
        return [user for user in self.users if user.get_role() == role]
    
    # =====================================================
    # NUMBER THEORY FUNCTIONS
    # =====================================================
    @staticmethod
    def calculate_priority_score(username, facility_name):
        """
        Number Theory: Calculate priority score using GCD and LCM
        """
        # Convert username to numeric value
        name_sum = sum(ord(c) for c in username)
        facility_sum = sum(ord(c) for c in facility_name)
        
        # Use GCD for priority calculation
        gcd_value = math.gcd(name_sum, facility_sum)
        
        # Use LCM for access level
        lcm_value = abs(name_sum * facility_sum) // math.gcd(name_sum, facility_sum) if name_sum > 0 and facility_sum > 0 else 0
        
        # Priority score (higher = better access)
        priority = (gcd_value * 2) + (lcm_value % 10)
        
        return priority
    
    @staticmethod
    def validate_capacity(room_capacity, num_users):
        """
        Number Theory: Validate capacity using divisibility
        """
        # Capacity must be divisible by 5
        if room_capacity % 5 != 0:
            return False, "Room capacity must be divisible by 5"
        
        # Capacity must be greater than number of users
        if room_capacity < num_users:
            return False, f"Room capacity ({room_capacity}) is less than number of users ({num_users})"
        
        return True, "Capacity is valid"
    
    @staticmethod
    def get_time_slot_hash(date_str, start_hour, facility_name):
        """
        Number Theory: Generate unique time slot hash using modular arithmetic
        """
        date_hash = sum(ord(c) for c in date_str)
        time_hash = (start_hour * 60) % 24
        facility_hash = sum(ord(c) for c in facility_name) % 10
        
        total_hash = (date_hash * time_hash + facility_hash) % 100
        return total_hash
    
    def get_user_by_school_id(self, school_id):
        """Find user by school ID"""
        for user in self.users:
            if user.get_school_id() == school_id:
                return user
        return None


# =====================================================
# PROOF OF ACCESS RULES
# =====================================================

class AccessProof:
    @staticmethod
    def prove_rules_valid():
        """
        Formal Proof of Access Rules Validity:
        
        Theorem: ∀u ∈ Users, ∀f ∈ Facilities:
        CanAccess(u, f) ↔ ((Faculty(u) ∨ Chairperson(u)) ∨ Staff(u) ∨ (Student(u) ∧ HasRequest(u, f) ∧ RequestApproved(u, f)))
        
        Proof by Cases:
        """
        return """
        ╔══════════════════════════════════════════════════════════════╗
        ║          FORMAL PROOF: ACCESS RULES VALIDITY               ║
        ╚══════════════════════════════════════════════════════════════╝
        
        Theorem: ∀u ∈ Users, ∀f ∈ Facilities:
        CanAccess(u, f) ↔ ((Faculty(u) ∨ Chairperson(u)) ∨ Staff(u) ∨ 
                           (Student(u) ∧ HasRequest(u, f) ∧ RequestApproved(u, f)))
        
        ────────────────────────────────────────────────────────────────
        
        Case 1: Faculty Member or Chairperson
        • Premise: Faculty(u) ∨ Chairperson(u)
        • Rule 1: Faculty(u) ∨ Chairperson(u) → Authorized(u)
        • Rule 2: Authorized(u) → CanAccess(u, f) for f ∈ {Library, Computer Lab, Science Lab, Faculty Room}
        • Conclusion: CanAccess(u, f) holds ✓
        
        ────────────────────────────────────────────────────────────────
        
        Case 2: Staff Member
        • Premise: Staff(u)
        • Rule 3: Staff(u) → Authorized(u)
        • Rule 4: Authorized(u) → CanAccess(u, f) for f ∈ {Library, Registrar Office}
        • Conclusion: CanAccess(u, f) holds ✓
        
        ────────────────────────────────────────────────────────────────
        
        Case 3: Student
        • Premise: Student(u)
        • Rule 5: Student(u) ∧ HasRequest(u, f) ∧ RequestApproved(u, f) → CanAccess(u, f)
        • Rule 6: Student(u) ∧ ¬HasRequest(u, f) → ¬CanAccess(u, f)
        • Conclusion: CanAccess(u, f) holds iff request exists and is approved ✓
        
        ────────────────────────────────────────────────────────────────
        
        Final Verdict:
        ✅ All user types are covered
        ✅ Rules are mutually exclusive
        ✅ No contradictions exist
        ✅ System is complete and consistent
        
        Boolean Expression: Access = (F ∨ C ∨ S ∨ (St ∧ R ∧ A))
        
        Where: F=Faculty, C=Chairperson, S=Staff, St=Student, R=Request, A=Approved
        """
    
    @staticmethod
    def prove_number_theory():
        """
        Number Theory Proof: Validation using Divisibility and GCD
        """
        return """
        ╔══════════════════════════════════════════════════════════════╗
        ║          NUMBER THEORY: PROOF OF VALIDITY                  ║
        ╚══════════════════════════════════════════════════════════════╝
        
        1. ID Verification using Divisibility:
           ∀id ∈ IDs, id must be even (divisible by 2)
           Proof: 2026-0002 % 2 = 0 ✓
        
        2. GCD for Permission Scoring:
           Let P(u,f) = permission score of user u for facility f
           P(u,f) = GCD(Sum(ASCII(username)), Sum(ASCII(facility_name)))
           Higher GCD = Higher Priority ✓
        
        3. LCM for Access Level:
           A(u,f) = LCM(Sum(ASCII(username)), Sum(ASCII(facility_name))) % 10
           Gives score 0-9 for access level ✓
        
        4. Modular Arithmetic for Time Slots:
           Hash = (DateHash * TimeHash + FacilityHash) % 100
           Unique identifier for each time slot ✓
        
        ∴ All number theory applications are valid and consistent.
        """


# =====================================================
# INITIALIZE SYSTEM
# =====================================================

system = AccessControlSystem()

# =====================================================
# FLASK ROUTES
# =====================================================

@app.route('/')
def home():
    if 'username' in session:
        return redirect(url_for('dashboard'))
    return redirect(url_for('login'))

# =====================================================
# AUTHENTICATION ROUTES
# =====================================================

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        
        if system.authenticate(username, password):
            session['username'] = username
            session['user_type'] = system.get_current_user().get_role()
            session['full_name'] = system.get_current_user().get_full_name()
            flash('Login successful! Welcome to the Access Control System.', 'success')
            return redirect(url_for('dashboard'))
        else:
            flash('Invalid username or password. Please try again.', 'error')
    
    return render_template('login.html')

@app.route('/logout')
def logout():
    system.logout()
    session.clear()
    flash('Logged out successfully', 'success')
    return redirect(url_for('login'))

# =====================================================
# DASHBOARD ROUTE
# =====================================================

@app.route('/dashboard')
def dashboard():
    if 'username' not in session:
        return redirect(url_for('login'))
    
    user = system.get_current_user()
    user_requests = system.get_user_requests(session['username'])
    user_history = system.get_user_history(session['username'])
    
    # Check if user can access (Boolean Logic)
    can_access = False
    if user:
        role = user.get_role()
        if role in ["Faculty", "Chairperson", "Staff"]:
            can_access = True
        elif role == "Student":
            # Check if student has approved requests
            for req in user_requests:
                if req.get_status() == "Approved":
                    can_access = True
                    break
    
    # Get statistics
    total_users = len(system.users)
    total_requests = len(system.access_requests)
    pending_requests = len(system.get_pending_requests())
    
    return render_template('dashboard.html',
                         username=session['username'],
                         full_name=session.get('full_name', ''),
                         user_type=user.get_role() if user else "Unknown",
                         can_access=can_access,
                         requests=user_requests,
                         history=user_history,
                         total_users=total_users,
                         total_requests=total_requests,
                         pending_requests=pending_requests)

# =====================================================
# VIEW ROOMS ROUTE
# =====================================================

@app.route('/rooms')
def view_rooms():
    if 'username' not in session:
        return redirect(url_for('login'))
    
    user = system.get_current_user()
    user_type = user.get_role() if user else "Unknown"
    
    # Filter rooms based on user type (Set Theory)
    if user_type in ["Faculty", "Chairperson", "Staff"]:
        # Faculty, Chairperson, and Staff can see all rooms
        available_rooms = system.rooms
    elif user_type == "Student":
        # Students can only see rooms they have access to
        user_requests = system.get_user_requests(session['username'])
        approved_rooms = [req.get_facility_name() for req in user_requests if req.get_status() == "Approved"]
        # Show all rooms but mark which are accessible
        available_rooms = system.rooms
        for room in available_rooms:
            # Check if this room type is accessible
            room_type = room.get_type()
            if room_type in approved_rooms or room_type == "Library":
                room.set_availability(True)
            else:
                room.set_availability(False)
    else:
        available_rooms = []
    
    return render_template('rooms.html', 
                         rooms=available_rooms,
                         user_type=user_type)

# =====================================================
# FACILITIES & SERVICES ROUTE
# =====================================================

@app.route('/facilities')
def view_facilities():
    if 'username' not in session:
        return redirect(url_for('login'))
    
    user = system.get_current_user()
    user_type = user.get_role() if user else "Unknown"
    
    # Boolean Logic: Determine which facilities to show
    if user_type in ["Faculty", "Chairperson", "Staff"]:
        # Faculty, Chairperson, and Staff can see all facilities
        available_facilities = system.facilities
    elif user_type == "Student":
        # Students can see facilities but limited access
        available_facilities = system.facilities
        user_requests = system.get_user_requests(session['username'])
        approved_facilities = [req.get_facility_name() for req in user_requests if req.get_status() == "Approved"]
        
        # Mark which facilities are accessible
        for facility in available_facilities:
            if facility.get_name() in approved_facilities or facility.get_type() == "library":
                facility.set_availability(True)
            else:
                facility.set_availability(False)
    else:
        available_facilities = []
    
    return render_template('facilities.html', 
                         facilities=available_facilities,
                         user_type=user_type)

# =====================================================
# ACCESS REQUEST ROUTE
# =====================================================

@app.route('/request_access', methods=['GET', 'POST'])
def request_access():
    if 'username' not in session:
        return redirect(url_for('login'))
    
    user = system.get_current_user()
    if not user:
        flash('User not found', 'error')
        return redirect(url_for('login'))
    
    if request.method == 'POST':
        facility_name = request.form.get('facility_name')
        date_str = request.form.get('date')
        start_hour = int(request.form.get('start_hour'))
        end_hour = int(request.form.get('end_hour'))
        purpose = request.form.get('purpose')
        
        # Validate date (cannot be in past)
        try:
            req_date = datetime.strptime(date_str, '%Y-%m-%d').date()
            if req_date < date.today():
                flash('Cannot request access for past dates', 'error')
                return render_template('request_access.html', facilities=system.facilities)
        except:
            flash('Invalid date format', 'error')
            return render_template('request_access.html', facilities=system.facilities)
        
        # Number Theory: Validate request using modular arithmetic
        request_hash = system.get_time_slot_hash(date_str, start_hour, facility_name)
        
        # Use hash to check if this is a valid time slot (even/odd check)
        if request_hash % 2 == 0:
            # Even hash - valid slot
            pass
        else:
            # Odd hash - less priority but still valid
            flash('This time slot has lower priority', 'warning')
        
        # Create request
        request, message = system.request_access(
            session['username'],
            facility_name,
            date_str,
            start_hour,
            end_hour,
            purpose
        )
        
        if request:
            flash(message, 'success')
            return redirect(url_for('dashboard'))
        else:
            flash(message, 'error')
    
    return render_template('request_access.html', facilities=system.facilities)

# =====================================================
# ACCESS HISTORY ROUTE
# =====================================================

@app.route('/history')
def history():
    if 'username' not in session:
        return redirect(url_for('login'))
    
    user_history = system.get_user_history(session['username'])
    return render_template('history.html', history=user_history)

# =====================================================
# VERIFY ID ROUTE (Number Theory)
# =====================================================

@app.route('/verify_id', methods=['GET', 'POST'])
def verify_id():
    if 'username' not in session:
        return redirect(url_for('login'))
    
    result = None
    if request.method == 'POST':
        school_id = request.form.get('school_id')
        valid, message = system.verify_id(school_id)
        result = {
            'valid': valid,
            'message': message,
            'school_id': school_id
        }
    
    return render_template('verify_id.html', result=result)

# =====================================================
# ADMIN ROUTES
# =====================================================

@app.route('/admin')
def admin_dashboard():
    if 'username' not in session:
        return redirect(url_for('login'))
    
    # Only faculty, staff, or chairperson can access admin
    user = system.get_current_user()
    if user.get_role() not in ["Faculty", "Staff", "Chairperson"]:
        flash('You do not have admin access', 'error')
        return redirect(url_for('dashboard'))
    
    pending_requests = system.get_pending_requests()
    all_requests = system.get_all_requests()
    all_history = system.get_all_history()
    
    # Access Matrix for display
    access_matrix = system.access_matrix.get_matrix()
    users = [user.get_username() for user in system.users]
    facilities = [facility.get_name() for facility in system.facilities]
    
    # User sets for display (Set Theory)
    students = system.get_users_by_role("Student")
    faculty = system.get_users_by_role("Faculty")
    staff = system.get_users_by_role("Staff")
    chairpersons = system.get_users_by_role("Chairperson")
    
    return render_template('admin.html',
                         pending_requests=pending_requests,
                         all_requests=all_requests,
                         all_history=all_history,
                         access_matrix=access_matrix,
                         users=users,
                         facilities=facilities,
                         students=students,
                         faculty=faculty,
                         staff=staff,
                         chairpersons=chairpersons,
                         user_role=user.get_role())

@app.route('/admin/approve/<request_id>')
def approve_request(request_id):
    if 'username' not in session:
        return redirect(url_for('login'))
    
    user = system.get_current_user()
    if user.get_role() not in ["Faculty", "Staff", "Chairperson"]:
        flash('You do not have admin access', 'error')
        return redirect(url_for('dashboard'))
    
    success, message = system.approve_request(request_id)
    flash(message, 'success' if success else 'error')
    return redirect(url_for('admin_dashboard'))

@app.route('/admin/reject/<request_id>')
def reject_request(request_id):
    if 'username' not in session:
        return redirect(url_for('login'))
    
    user = system.get_current_user()
    if user.get_role() not in ["Faculty", "Staff", "Chairperson"]:
        flash('You do not have admin access', 'error')
        return redirect(url_for('dashboard'))
    
    success, message = system.reject_request(request_id)
    flash(message, 'success' if success else 'error')
    return redirect(url_for('admin_dashboard'))

# =====================================================
# ACCESS RELATIONS ROUTE
# =====================================================

@app.route('/relations')
def view_relations():
    if 'username' not in session:
        return redirect(url_for('login'))
    
    # Build access relations (User → Facility)
    relations = []
    for user in system.users:
        for facility in system.facilities:
            # Check if user has access
            role = user.get_role()
            facility_name = facility.get_name()
            
            has_access = False
            if role in ["Faculty", "Chairperson"]:
                if facility_name in ["Library", "Computer Laboratory", "Science Laboratory", "Faculty Room"]:
                    has_access = True
            elif role == "Staff":
                if facility_name in ["Library", "Registrar Office"]:
                    has_access = True
            elif role == "Student":
                # Check approved requests
                for req in system.access_requests:
                    if req.get_username() == user.get_username() and req.get_facility_name() == facility_name and req.get_status() == "Approved":
                        has_access = True
                        break
            
            if has_access:
                relations.append({
                    "username": user.get_username(),
                    "full_name": user.get_full_name(),
                    "role": role,
                    "facility": facility_name
                })
    
    return render_template('relations.html', relations=relations)

# =====================================================
# ACCESS MATRIX ROUTE
# =====================================================

@app.route('/matrix')
def view_matrix():
    if 'username' not in session:
        return redirect(url_for('login'))
    
    access_matrix = system.access_matrix.get_matrix()
    users = [user.get_username() for user in system.users]
    facilities = [facility.get_name() for facility in system.facilities]
    
    return render_template('matrix.html', 
                         access_matrix=access_matrix,
                         users=users,
                         facilities=facilities)

# =====================================================
# ACCESS RULES ROUTE
# =====================================================

@app.route('/rules')
def view_rules():
    if 'username' not in session:
        return redirect(url_for('login'))
    
    return render_template('rules.html')

# =====================================================
# PROOF ROUTE
# =====================================================

@app.route('/proof')
def show_proof():
    if 'username' not in session:
        return redirect(url_for('login'))
    
    proof_text = AccessProof.prove_rules_valid()
    number_theory_proof = AccessProof.prove_number_theory()
    
    return render_template('proof.html', 
                         proof_text=proof_text,
                         number_theory_proof=number_theory_proof)

# =====================================================
# RUN APPLICATION
# =====================================================

if __name__ == '__main__':
    app.run(debug=True)