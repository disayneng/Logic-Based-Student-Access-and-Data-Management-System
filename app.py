from flask import Flask, render_template, request, redirect, url_for, session, flash, jsonify
from datetime import datetime, date, timedelta
import math
import os
import random
import hashlib
import base64
from collections import deque
import json

app = Flask(__name__)
app.secret_key = os.environ.get('SECRET_KEY', 'secure_campus_final_2026')

# =====================================================
# CRYPTOGRAPHY FEATURE
# =====================================================

class Cryptography:
    """Simple Caesar cipher with shifting for secure messages"""
    
    @staticmethod
    def encrypt(text, shift=3):
        """Encrypt text using Caesar cipher"""
        result = ""
        for char in text:
            if char.isupper():
                result += chr((ord(char) + shift - 65) % 26 + 65)
            elif char.islower():
                result += chr((ord(char) + shift - 97) % 26 + 97)
            else:
                result += char
        return result
    
    @staticmethod
    def decrypt(text, shift=3):
        """Decrypt text using Caesar cipher"""
        result = ""
        for char in text:
            if char.isupper():
                result += chr((ord(char) - shift - 65) % 26 + 65)
            elif char.islower():
                result += chr((ord(char) - shift - 97) % 26 + 97)
            else:
                result += char
        return result
    
    @staticmethod
    def hash_password(password):
        """Hash password using SHA-256"""
        return hashlib.sha256(password.encode()).hexdigest()
    
    @staticmethod
    def verify_password(password, hashed):
        """Verify password against hash"""
        return Cryptography.hash_password(password) == hashed
    
    @staticmethod
    def generate_secure_code(length=6):
        """Generate a secure access code"""
        chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
        code = ''.join(random.choice(chars) for _ in range(length))
        return code

# =====================================================
# SEARCHING AND SORTING ALGORITHMS
# =====================================================

class SearchAndSort:
    """Searching and sorting algorithms for records"""
    
    @staticmethod
    def binary_search(users, target_username):
        """Binary search for user by username"""
        sorted_users = sorted(users, key=lambda u: u.username)
        left, right = 0, len(sorted_users) - 1
        
        while left <= right:
            mid = (left + right) // 2
            if sorted_users[mid].username == target_username:
                return sorted_users[mid]
            elif sorted_users[mid].username < target_username:
                left = mid + 1
            else:
                right = mid - 1
        return None
    
    @staticmethod
    def quick_sort(arr, key=lambda x: x):
        """Quick sort implementation"""
        if len(arr) <= 1:
            return arr
        pivot = arr[len(arr) // 2]
        left = [x for x in arr if key(x) < key(pivot)]
        middle = [x for x in arr if key(x) == key(pivot)]
        right = [x for x in arr if key(x) > key(pivot)]
        return SearchAndSort.quick_sort(left, key) + middle + SearchAndSort.quick_sort(right, key)
    
    @staticmethod
    def linear_search(records, key, value):
        """Linear search for records"""
        results = []
        for record in records:
            if getattr(record, key, None) == value:
                results.append(record)
        return results

# =====================================================
# RECURSION - Route Exploration and Tree Traversal
# =====================================================

class RecursiveFunctions:
    """Recursive functions for route exploration and tree traversal"""
    
    @staticmethod
    def find_path(graph, start, end, path=None):
        """Recursive DFS to find path between nodes"""
        if path is None:
            path = []
        path = path + [start]
        
        if start == end:
            return path
        
        if start not in graph:
            return None
        
        for node in graph[start]:
            if node not in path:
                new_path = RecursiveFunctions.find_path(graph, node, end, path)
                if new_path:
                    return new_path
        return None
    
    @staticmethod
    def find_all_paths(graph, start, end, path=None):
        """Recursive function to find all paths"""
        if path is None:
            path = []
        path = path + [start]
        
        if start == end:
            return [path]
        
        if start not in graph:
            return []
        
        paths = []
        for node in graph[start]:
            if node not in path:
                new_paths = RecursiveFunctions.find_all_paths(graph, node, end, path)
                for p in new_paths:
                    paths.append(p)
        return paths
    
    @staticmethod
    def factorial(n):
        """Recursive factorial for probability calculations"""
        if n <= 1:
            return 1
        return n * RecursiveFunctions.factorial(n - 1)
    
    @staticmethod
    def combinations(n, r):
        """Recursive combination calculation"""
        if r == 0 or r == n:
            return 1
        return RecursiveFunctions.combinations(n - 1, r - 1) + RecursiveFunctions.combinations(n - 1, r)

# =====================================================
# PROBABILITY AND COUNTING METHODS
# =====================================================

class ProbabilityCalculator:
    """Counting methods and discrete probability"""
    
    @staticmethod
    def room_availability_probability(total_rooms, occupied_rooms):
        """Calculate probability of room availability"""
        if total_rooms == 0:
            return 0
        return (total_rooms - occupied_rooms) / total_rooms
    
    @staticmethod
    def access_success_probability(total_attempts, successful_attempts):
        """Calculate probability of access success"""
        if total_attempts == 0:
            return 0
        return successful_attempts / total_attempts
    
    @staticmethod
    def route_options_probability(total_paths, viable_paths):
        """Calculate probability of finding viable route"""
        if total_paths == 0:
            return 0
        return viable_paths / total_paths
    
    @staticmethod
    def permutation(n, r):
        """Calculate permutations (ordered arrangements)"""
        if r > n:
            return 0
        return RecursiveFunctions.factorial(n) // RecursiveFunctions.factorial(n - r)
    
    @staticmethod
    def expected_value(probabilities, values):
        """Calculate expected value"""
        if len(probabilities) != len(values):
            return 0
        return sum(p * v for p, v in zip(probabilities, values))

# =====================================================
# RANDOM VARIABLES
# =====================================================

class RandomVariables:
    """Random variables for system analysis"""
    
    @staticmethod
    def simulate_user_arrival(rate=5, time_period=60):
        """Simulate user arrivals using Poisson-like distribution"""
        arrivals = []
        current_time = 0
        while current_time < time_period:
            wait_time = random.expovariate(1.0 / rate)
            current_time += wait_time
            if current_time < time_period:
                arrivals.append(int(current_time))
        return arrivals
    
    @staticmethod
    def simulate_room_availability(room_count, occupation_rate=0.7):
        """Simulate room availability"""
        occupied = random.randint(0, room_count)
        available = room_count - occupied
        return {
            'total': room_count,
            'occupied': occupied,
            'available': available,
            'availability_rate': available / room_count if room_count > 0 else 0
        }
    
    @staticmethod
    def generate_waiting_times(num_samples=10, mean=5):
        """Generate random waiting times (exponential distribution)"""
        return [random.expovariate(1.0 / mean) for _ in range(num_samples)]
    
    @staticmethod
    def route_status_random(navigation_count, total_possible=10):
        """Generate random route status"""
        return {
            'active_routes': random.randint(0, min(navigation_count, total_possible)),
            'successful_navigations': random.randint(0, navigation_count),
            'failed_navigations': random.randint(0, max(0, navigation_count - 1))
        }

# =====================================================
# GRAPH - Campus Navigation
# =====================================================

class CampusGraph:
    """Graph representation of campus locations and paths"""
    
    def __init__(self):
        self.adjacency_list = {}
        self.locations = {}
        self._initialize_graph()
    
    def _initialize_graph(self):
        """Initialize campus graph with locations and connections"""
        locations = [
            ('Main Gate', 0, 0),
            ('Admin Building', 2, 1),
            ('Library', 3, 3),
            ('Computer Lab 1', 5, 1),
            ('Computer Lab 2', 6, 2),
            ('Faculty Office', 4, 4),
            ('Registrar Office', 3, 5),
            ('Science Lab', 6, 4),
            ('Lecture Room 1', 1, 3),
            ('Lecture Room 2', 1, 5),
            ('Cafeteria', 4, 6),
            ('Student Center', 2, 6),
        ]
        
        for name, x, y in locations:
            self.add_location(name, x, y)
        
        edges = [
            ('Main Gate', 'Admin Building', 2.5),
            ('Main Gate', 'Library', 3.0),
            ('Admin Building', 'Library', 1.5),
            ('Admin Building', 'Computer Lab 1', 3.0),
            ('Admin Building', 'Lecture Room 1', 1.5),
            ('Library', 'Faculty Office', 2.0),
            ('Library', 'Lecture Room 1', 2.0),
            ('Library', 'Registrar Office', 2.5),
            ('Computer Lab 1', 'Computer Lab 2', 1.5),
            ('Computer Lab 1', 'Faculty Office', 3.5),
            ('Computer Lab 2', 'Science Lab', 2.0),
            ('Faculty Office', 'Registrar Office', 2.0),
            ('Faculty Office', 'Science Lab', 2.5),
            ('Registrar Office', 'Cafeteria', 2.0),
            ('Registrar Office', 'Student Center', 2.0),
            ('Science Lab', 'Cafeteria', 2.0),
            ('Lecture Room 1', 'Lecture Room 2', 2.0),
            ('Lecture Room 2', 'Student Center', 2.0),
            ('Student Center', 'Cafeteria', 2.0),
        ]
        
        for from_loc, to_loc, distance in edges:
            self.add_edge(from_loc, to_loc, distance)
    
    def add_location(self, name, x, y):
        """Add a location to the graph"""
        self.locations[name] = {'x': x, 'y': y}
        if name not in self.adjacency_list:
            self.adjacency_list[name] = []
    
    def add_edge(self, from_loc, to_loc, distance):
        """Add an edge between two locations"""
        if from_loc not in self.adjacency_list:
            self.adjacency_list[from_loc] = []
        if to_loc not in self.adjacency_list:
            self.adjacency_list[to_loc] = []
        
        self.adjacency_list[from_loc].append((to_loc, distance))
        self.adjacency_list[to_loc].append((from_loc, distance))
    
    def get_neighbors(self, location):
        """Get neighbors of a location"""
        return self.adjacency_list.get(location, [])
    
    def get_locations(self):
        """Get all locations"""
        return list(self.locations.keys())
    
    def get_location_coords(self, location):
        """Get coordinates of a location"""
        return self.locations.get(location, {'x': 0, 'y': 0})
    
    def find_shortest_path(self, start, end):
        """Find shortest path using Dijkstra's algorithm"""
        if start not in self.adjacency_list or end not in self.adjacency_list:
            return None
        
        distances = {loc: float('inf') for loc in self.adjacency_list}
        previous = {loc: None for loc in self.adjacency_list}
        distances[start] = 0
        unvisited = set(self.adjacency_list.keys())
        
        while unvisited:
            current = min(unvisited, key=lambda loc: distances[loc])
            if distances[current] == float('inf'):
                break
            
            unvisited.remove(current)
            
            if current == end:
                break
            
            for neighbor, distance in self.adjacency_list[current]:
                if neighbor in unvisited:
                    new_distance = distances[current] + distance
                    if new_distance < distances[neighbor]:
                        distances[neighbor] = new_distance
                        previous[neighbor] = current
        
        path = []
        current = end
        while current is not None:
            path.insert(0, current)
            current = previous[current]
        
        if path[0] != start:
            return None
        
        return {
            'path': path,
            'distance': distances[end]
        }

# =====================================================
# TREE - Department and Room Organization
# =====================================================

class TreeNode:
    """Node for tree organization"""
    
    def __init__(self, name, data=None):
        self.name = name
        self.data = data
        self.children = []
        self.parent = None
    
    def add_child(self, child):
        """Add a child node"""
        child.parent = self
        self.children.append(child)
        return child
    
    def remove_child(self, child):
        """Remove a child node"""
        if child in self.children:
            self.children.remove(child)
            child.parent = None
    
    def find(self, name):
        """Find a node by name (recursive)"""
        if self.name == name:
            return self
        for child in self.children:
            result = child.find(name)
            if result:
                return result
        return None
    
    def get_path(self):
        """Get path from root to this node"""
        path = []
        current = self
        while current:
            path.insert(0, current.name)
            current = current.parent
        return path
    
    def to_dict(self):
        """Convert tree to dictionary"""
        return {
            'name': self.name,
            'data': self.data,
            'children': [child.to_dict() for child in self.children]
        }

class CampusTree:
    """Tree structure for campus organization"""
    
    def __init__(self):
        self.root = TreeNode("Campus")
        self._build_tree()
    
    def _build_tree(self):
        """Build the campus organization tree"""
        depts = {
            "CCS": self.root.add_child(TreeNode("College of Computer Studies")),
            "COE": self.root.add_child(TreeNode("College of Engineering")),
            "CBM": self.root.add_child(TreeNode("College of Business Management")),
        }
        
        ccs = depts["CCS"]
        ccs.add_child(TreeNode("Computer Science"))
        ccs.add_child(TreeNode("Information Technology"))
        ccs.add_child(TreeNode("Computer Engineering"))
        
        coe = depts["COE"]
        coe.add_child(TreeNode("Mechanical Engineering"))
        coe.add_child(TreeNode("Electrical Engineering"))
        coe.add_child(TreeNode("Civil Engineering"))
        
        cbm = depts["CBM"]
        cbm.add_child(TreeNode("Business Administration"))
        cbm.add_child(TreeNode("Marketing"))
        cbm.add_child(TreeNode("Finance"))
        
        rooms = [
            ("Computer Science", "CS Lab 1"),
            ("Computer Science", "CS Lab 2"),
            ("Computer Science", "CS Lecture Room"),
            ("Information Technology", "IT Lab"),
            ("Information Technology", "IT Lecture Room"),
            ("Computer Engineering", "CE Lab"),
            ("Mechanical Engineering", "ME Workshop"),
            ("Mechanical Engineering", "ME Lab"),
            ("Electrical Engineering", "EE Lab"),
            ("Civil Engineering", "CE Studio"),
            ("Business Administration", "BA Classroom 1"),
            ("Business Administration", "BA Classroom 2"),
            ("Marketing", "Marketing Lab"),
            ("Finance", "Finance Lab"),
        ]
        
        for dept_name, room_name in rooms:
            dept_node = self.root.find(dept_name)
            if dept_node:
                dept_node.add_child(TreeNode(room_name))
    
    def get_rooms(self):
        """Get all rooms in the tree"""
        rooms = []
        self._collect_rooms(self.root, rooms)
        return rooms
    
    def _collect_rooms(self, node, rooms):
        """Collect rooms recursively"""
        if not node.children:
            rooms.append(node.name)
        for child in node.children:
            self._collect_rooms(child, rooms)
    
    def get_departments(self):
        """Get all departments"""
        return [child.name for child in self.root.children]
    
    def get_rooms_by_department(self, department):
        """Get rooms for a specific department"""
        dept = self.root.find(department)
        if not dept:
            return []
        rooms = []
        for child in dept.children:
            if not child.children:
                rooms.append(child.name)
        return rooms
    
    def traverse_preorder(self, node=None):
        """Preorder traversal (recursive)"""
        if node is None:
            node = self.root
        
        result = [node.name]
        for child in node.children:
            result.extend(self.traverse_preorder(child))
        return result
    
    def traverse_postorder(self, node=None):
        """Postorder traversal (recursive)"""
        if node is None:
            node = self.root
        
        result = []
        for child in node.children:
            result.extend(self.traverse_postorder(child))
        result.append(node.name)
        return result

# =====================================================
# FINITE STATE MACHINE
# =====================================================

class FiniteStateMachine:
    """Finite State Machine for system states"""
    
    STATES = {
        'IDLE': 'Idle',
        'LOGIN': 'Login',
        'ACCESS_GRANTED': 'Access Granted',
        'ACCESS_DENIED': 'Access Denied',
        'NAVIGATING': 'Navigating',
        'MONITORING': 'Monitoring',
        'EXIT': 'Exit'
    }
    
    def __init__(self):
        self.state = self.STATES['IDLE']
        self.state_history = []
        self.transition_rules = self._init_transition_rules()
    
    def _init_transition_rules(self):
        """Initialize FSM transition rules"""
        return {
            self.STATES['IDLE']: ['LOGIN', 'EXIT'],
            self.STATES['LOGIN']: ['ACCESS_GRANTED', 'ACCESS_DENIED'],
            self.STATES['ACCESS_GRANTED']: ['NAVIGATING', 'MONITORING', 'EXIT'],
            self.STATES['ACCESS_DENIED']: ['IDLE', 'EXIT'],
            self.STATES['NAVIGATING']: ['MONITORING', 'EXIT', 'IDLE'],
            self.STATES['MONITORING']: ['NAVIGATING', 'EXIT', 'IDLE'],
            self.STATES['EXIT']: ['IDLE']
        }
    
    def transition(self, new_state):
        """Transition to a new state if valid"""
        if new_state not in self.transition_rules.get(self.state, []):
            return False, f"Invalid transition from {self.state} to {new_state}"
        
        self.state_history.append(self.state)
        self.state = new_state
        return True, f"Transitioned to {new_state}"
    
    def get_state(self):
        """Get current state"""
        return self.state
    
    def get_history(self):
        """Get state history"""
        return self.state_history
    
    def reset(self):
        """Reset to idle state"""
        self.state = self.STATES['IDLE']
        self.state_history = []

# =====================================================
# PROGRAM OPTIONS FOR REGISTRATION
# =====================================================

PROGRAM_OPTIONS = {
    "COLLEGE OF SCIENCE AND MANAGEMENT": [
        ("BSCS", "BACHELOR OF SCIENCE IN COMPUTER SCIENCE"),
        ("BSES", "BACHELOR OF SCIENCE IN ENVIRONMENTAL SCIENCE"),
        ("BSHM", "BACHELOR OF SCIENCE IN HOSPITALITY MANAGEMENT"),
    ],
    "COLLEGE OF TEACHER EDUCATION": [
        ("BEED", "BACHELOR OF EDUCATION IN ELEMENTARY EDUCATION"),
        ("BSED-MATH", "BACHELOR OF SECONDARY EDUCATION - MAJOR IN MATHEMATICS"),
        ("BTLED-HE", "BACHELOR OF TECHNOLOGICAL EDUCATION - MAJOR IN HOME ECONOMICS"),
    ]
}

# =====================================================
# ROOM PROGRAM MAPPING
# =====================================================

ROOM_PROGRAM_MAPPING = {
    # CSM - College of Science and Management
    "COMLAB 1": "BSCS",
    "COMLAB 2": "BSCS",
    "COMLAB 3": "BSCS",
    "COMLAB 4": "BSCS",
    "COMLEC 1": "BSCS",
    "COMLEC 2": "BSCS",
    "S&T LAB 1": "BSES",
    "S&T LAB 2": "BSES",
    "HOT KITCHEN": "BSHM",
    "COLD KITCHEN": "BSHM",
    "HM ROOM 1": "BSHM",
    "HM ROOM 2": "BSHM",
    "HM ROOM 3": "BSHM",
    "HM ROOM 4": "BSHM",
    "S&T LAB": "BSES",
    # CTE - College of Teacher Education
    "CTE ROOM 1": "BEED",
    "CTE ROOM 2": "BEED",
    "CTE ROOM 3": "BEED",
    "CTE ROOM 4": "BEED",
    "CTE ROOM 5": "BEED",
    "CTE ROOM 6": "BEED",
    "CTE ROOM 7": "BEED",
    "CTE ROOM 8": "BEED",
    "CTE LAB 1": "BSED-MATH",
    "CTE LAB 2": "BSED-MATH",
    "CTE LAB 3": "BTLED-HE",
    "CTE LAB 4": "BTLED-HE",
    "SPEECH LAB": "BEED",
    # General
    "ES ROOM 1": "BSES",
    "ES ROOM 2": "BSES",
    "ES ROOM 3": "BSES",
    "ES ROOM 4": "BSES",
    "ES ROOM 5": "BSES",
    "CSM OFFICE": "CSM",
    "CTE OFFICE": "CTE",
}

# =====================================================
# DATA FROM PROVIDED TABLES
# =====================================================

USER_DATA = [
    {"school_id": "2026-0001", "username": "alexa.cortes", "role": "Student", "full_name": "Alexa Cortes", "password": "Student@123", "program": "BSCS"},
    {"school_id": "2026-0003", "username": "maria.santos", "role": "Faculty", "full_name": "Maria Santos", "password": "Faculty@123", "program": ""},
    {"school_id": "2026-0005", "username": "anna.garcia", "role": "Staff", "full_name": "Anna Garcia", "password": "Staff@123", "program": ""},
    {"school_id": "2026-0007", "username": "carlos.mendoza", "role": "Chairperson", "full_name": "Carlos Mendoza", "password": "Chair@123", "program": "", "chairperson_college": "COLLEGE OF SCIENCE AND MANAGEMENT"},
]

# =====================================================
# VISITOR, AUTHORIZED USER, AND RESTRICTED USER DATA
# =====================================================

# Visitors - Limited access, can only view public areas
VISITOR_DATA = [
    {"school_id": "2026-1001", "username": "visitor.juan", "full_name": "Juan Dela Cruz", "password": "Visitor@123", "role": "Visitor"},
    {"school_id": "2026-1002", "username": "visitor.maria", "full_name": "Maria Reyes", "password": "Visitor@123", "role": "Visitor"},
]

# Authorized Users - Have special access to specific rooms
AUTHORIZED_USER_DATA = [
    {"school_id": "2026-2001", "username": "auth.peter", "full_name": "Peter Parker", "password": "Auth@123", "role": "Student", "program": "BSCS", "authorized_rooms": ["COMLAB 1", "COMLAB 2", "LIBRARY"]},
    {"school_id": "2026-2002", "username": "auth.tony", "full_name": "Tony Stark", "password": "Auth@123", "role": "Student", "program": "BSES", "authorized_rooms": ["S&T LAB 1", "S&T LAB 2", "ES ROOM 1"]},
    {"school_id": "2026-2003", "username": "auth.natasha", "full_name": "Natasha Romanoff", "password": "Auth@123", "role": "Faculty", "program": "", "authorized_rooms": ["FACULTY OFFICE", "LIBRARY", "CTE LAB 1", "CTE LAB 2"]},
]

# Restricted Users - Have limited access, only specific rooms
RESTRICTED_USER_DATA = [
    {"school_id": "2026-3001", "username": "rest.steve", "full_name": "Steve Rogers", "password": "Rest@123", "role": "Visitor", "restricted_rooms": ["MAIN GATE", "ADMIN OFFICE"]},
    {"school_id": "2026-3002", "username": "rest.bucky", "full_name": "Bucky Barnes", "password": "Rest@123", "role": "Student", "program": "BTLED-HE", "restricted_rooms": ["CTE LAB 3", "CTE LAB 4"]},
]

ROOM_DATA = [
    # CS DEPARTMENT
    {"room_id": "RM-CSLAB-A01", "room_number": "COMLAB 1", "room_name": "COMLAB 1", "type": "Computer Laboratory"},
    {"room_id": "RM-CSLAB-A02", "room_number": "COMLAB 2", "room_name": "COMLAB 2", "type": "Computer Laboratory"},
    {"room_id": "RM-CSLAB-A03", "room_number": "COMLAB 3", "room_name": "COMLAB 3", "type": "Computer Laboratory"},
    {"room_id": "RM-CSLAB-A04", "room_number": "COMLAB 4", "room_name": "COMLAB 4", "type": "Computer Laboratory"},

    {"room_id": "RM-CSLEC-B01", "room_number": "COMLEC 1", "room_name": "COMLEC 1", "type": "Lecture Room"},
    {"room_id": "RM-CSLEC-B02", "room_number": "COMLEC 2", "room_name": "COMLEC 2", "type": "Lecture Room"},

    {"room_id": "RM-CSSLT-C01", "room_number": "S&T LAB 1", "room_name": "S&T LAB 1", "type": "Laboratory"},
    {"room_id": "RM-CSSLT-C02", "room_number": "S&T LAB 2", "room_name": "S&T LAB 2", "type": "Laboratory"},
    
    # CTE BUILDING
    {"room_id": "RM-CTERM-D01", "room_number": "CTE ROOM 1", "room_name": "CTE ROOM 1", "type": "Classroom"},
    {"room_id": "RM-CTERM-D02", "room_number": "CTE ROOM 2", "room_name": "CTE ROOM 2", "type": "Classroom"},
    {"room_id": "RM-CTERM-D03", "room_number": "CTE ROOM 3", "room_name": "CTE ROOM 3", "type": "Classroom"},
    {"room_id": "RM-CTERM-D04", "room_number": "CTE ROOM 4", "room_name": "CTE ROOM 4", "type": "Classroom"},
    {"room_id": "RM-CTERM-D05", "room_number": "CTE ROOM 5", "room_name": "CTE ROOM 5", "type": "Classroom"},
    {"room_id": "RM-CTERM-D06", "room_number": "CTE ROOM 6", "room_name": "CTE ROOM 6", "type": "Classroom"},
    {"room_id": "RM-CTERM-D07", "room_number": "CTE ROOM 7", "room_name": "CTE ROOM 7", "type": "Classroom"},
    {"room_id": "RM-CTERM-D08", "room_number": "CTE ROOM 8", "room_name": "CTE ROOM 8", "type": "Classroom"},

    {"room_id": "RM-CTELAB-E01", "room_number": "CTE LAB 1", "room_name": "CTE LAB 1", "type": "Laboratory"},
    {"room_id": "RM-CTELAB-E02", "room_number": "CTE LAB 2", "room_name": "CTE LAB 2", "type": "Laboratory"},
    {"room_id": "RM-CTELAB-E03", "room_number": "CTE LAB 3", "room_name": "CTE LAB 3", "type": "Laboratory"},
    {"room_id": "RM-CTELAB-E04", "room_number": "CTE LAB 4", "room_name": "CTE LAB 4", "type": "Laboratory"},

    {"room_id": "RM-CTESPEECH-F01", "room_number": "SPEECH LAB", "room_name": "SPEECH LAB", "type": "Laboratory"},

    # HM BUILDING
    {"room_id": "RM-HMHK-G01", "room_number": "HOT KITCHEN", "room_name": "HOT KITCHEN", "type": "Laboratory"},
    {"room_id": "RM-HMCK-G02", "room_number": "COLD KITCHEN", "room_name": "COLD KITCHEN", "type": "Laboratory"},

    {"room_id": "RM-HMROOM-H01", "room_number": "HM ROOM 1", "room_name": "HM ROOM 1", "type": "Classroom"},
    {"room_id": "RM-HMROOM-H02", "room_number": "HM ROOM 2", "room_name": "HM ROOM 2", "type": "Classroom"},
    {"room_id": "RM-HMROOM-H03", "room_number": "HM ROOM 3", "room_name": "HM ROOM 3", "type": "Classroom"},
    {"room_id": "RM-HMROOM-H04", "room_number": "HM ROOM 4", "room_name": "HM ROOM 4", "type": "Classroom"},

    {"room_id": "RM-HMSLT-I01", "room_number": "S&T LAB", "room_name": "S&T LAB", "type": "Laboratory"},

    # ES BUILDING
    {"room_id": "RM-ESROOM-J01", "room_number": "ES ROOM 1", "room_name": "ES ROOM 1", "type": "Classroom"},
    {"room_id": "RM-ESROOM-J02", "room_number": "ES ROOM 2", "room_name": "ES ROOM 2", "type": "Classroom"},
    {"room_id": "RM-ESROOM-J03", "room_number": "ES ROOM 3", "room_name": "ES ROOM 3", "type": "Classroom"},
    {"room_id": "RM-ESROOM-J04", "room_number": "ES ROOM 4", "room_name": "ES ROOM 4", "type": "Classroom"},
    {"room_id": "RM-ESROOM-J05", "room_number": "ES ROOM 5", "room_name": "ES ROOM 5", "type": "Classroom"},

    # OTHER ROOMS / FACILITIES
    {"room_id": "RM-SAC-K01", "room_number": "STUDENT ACTIVITY CENTER", "room_name": "STUDENT ACTIVITY CENTER", "type": "Activity Center"},
    {"room_id": "RM-SAS-L01", "room_number": "SAS OFFICE", "room_name": "SAS OFFICE", "type": "Office"},
    {"room_id": "RM-PROC-M01", "room_number": "PROCUREMENT OFFICE", "room_name": "PROCUREMENT OFFICE", "type": "Office"},
    {"room_id": "RM-ADMIN-N01", "room_number": "ADMIN OFFICE", "room_name": "ADMIN OFFICE", "type": "Office"},
    {"room_id": "RM-SERVER-O01", "room_number": "SERVER ROOM", "room_name": "SERVER ROOM", "type": "Technical Facility"},
    {"room_id": "RM-CLINIC-P01", "room_number": "CLINIC", "room_name": "CLINIC", "type": "Health Facility"},
    {"room_id": "RM-GUID-Q01", "room_number": "GUIDANCE OFFICE", "room_name": "GUIDANCE OFFICE", "type": "Office"},
    {"room_id": "RM-DNST-R01", "room_number": "DNST OFFICE", "room_name": "DNST OFFICE", "type": "Office"},
    {"room_id": "RM-ROTC-S01", "room_number": "ROTC OFFICE", "room_name": "ROTC OFFICE", "type": "Office"},
    {"room_id": "RM-ALUMNI-T01", "room_number": "ALUMNI OFFICE", "room_name": "ALUMNI OFFICE", "type": "Office"},
    {"room_id": "RM-FSTLP-U01", "room_number": "FSTLP OFFICE", "room_name": "FSTLP OFFICE", "type": "Office"},
    {"room_id": "RM-SDS-V01", "room_number": "SDS OFFICE", "room_name": "SDS OFFICE", "type": "Office"},
    {"room_id": "RM-SSG-W01", "room_number": "SSG OFFICE", "room_name": "SSG OFFICE", "type": "Office"},
    {"room_id": "RM-SCHOLAR-X01", "room_number": "SCHOLARSHIP OFFICE", "room_name": "SCHOLARSHIP OFFICE", "type": "Office"},
    {"room_id": "RM-CSM-Y01", "room_number": "CSM OFFICE", "room_name": "CSM OFFICE", "type": "Office"},
    {"room_id": "RM-FAC-Z01", "room_number": "FACULTY OFFICE", "room_name": "FACULTY OFFICE", "type": "Office"},
    {"room_id": "RM-AVR-AA01", "room_number": "AVR", "room_name": "AVR", "type": "Facility"},
    {"room_id": "RM-LIB-AB01", "room_number": "LIBRARY", "room_name": "LIBRARY", "type": "Library"},
    {"room_id": "RM-CTEOFF-AC01", "room_number": "CTE OFFICE", "room_name": "CTE OFFICE", "type": "Office"},
    {"room_id": "RM-ACC-AD01", "room_number": "ACCREDITATION CENTER", "room_name": "ACCREDITATION CENTER", "type": "Office"},
    {"room_id": "RM-PARAGON-AE01", "room_number": "PARAGON OFFICE", "room_name": "PARAGON OFFICE", "type": "Office"},
]

# =====================================================
# SET THEORY - User Classification Sets
# =====================================================

students = set()
faculty = set()
staff = set()
chairpersons = set()
visitors = set()
authorized_users = set()
restricted_users = set()

# =====================================================
# FACILITIES SET
# =====================================================

facilities_set = {"LIBRARY", "COMLAB 1", "COMLAB 2", "COMLAB 3", "COMLAB 4", "S&T LAB 1", "S&T LAB 2", "FACULTY OFFICE"}

# =====================================================
# USER STORAGE
# =====================================================

users = []
access_requests = []
access_history = []
current_user = None
fsm = FiniteStateMachine()

# =====================================================
# INITIALIZE CAMPUS GRAPH AND TREE
# =====================================================

campus_graph = CampusGraph()
campus_tree = CampusTree()

# =====================================================
# ACCESS MATRIX
# =====================================================

access_matrix = [
    [1, 1, 0, 0, 0],  # Student
    [1, 1, 1, 1, 0],  # Faculty
    [1, 0, 0, 0, 1],  # Staff
    [1, 1, 1, 1, 1],  # Chairperson
    [1, 0, 0, 0, 0],  # Visitor
    [1, 1, 1, 0, 0],  # Authorized User
    [0, 0, 0, 0, 0],  # Restricted User
]

role_to_row = {
    "Student": 0,
    "Faculty": 1,
    "Staff": 2,
    "Chairperson": 3,
    "Visitor": 4,
    "Authorized": 5,
    "Restricted": 6
}

facility_to_col = {
    "LIBRARY": 0,
    "COMLAB 1": 1,
    "COMLAB 2": 1,
    "COMLAB 3": 1,
    "COMLAB 4": 1,
    "S&T LAB 1": 2,
    "S&T LAB 2": 2,
    "FACULTY OFFICE": 3,
    "CSM OFFICE": 4,
}

# =====================================================
# USER CLASS
# =====================================================

class User:
    def __init__(self, school_id, username, password, role, full_name, program="", authorized_rooms=None, restricted_rooms=None):
        self.school_id = school_id
        self.username = username
        self.password = password
        self.password_hash = Cryptography.hash_password(password)
        self.role = role
        self.full_name = full_name
        self.program = program
        self.chairperson_college = ""
        self.is_authorized = False
        self.secure_code = Cryptography.generate_secure_code()
        self.access_count = 0
        self.user_type = "Standard"
        self.authorized_rooms = authorized_rooms or []
        self.restricted_rooms = restricted_rooms or []
    
    def verify_password(self, password):
        return Cryptography.verify_password(password, self.password_hash)
    
    def to_dict(self):
        return {
            "school_id": self.school_id,
            "username": self.username,
            "password": self.password,
            "role": self.role,
            "full_name": self.full_name,
            "program": self.program,
            "chairperson_college": self.chairperson_college,
            "authorized": self.is_authorized,
            "access_count": self.access_count,
            "user_type": self.user_type,
            "authorized_rooms": self.authorized_rooms,
            "restricted_rooms": self.restricted_rooms
        }

# =====================================================
# ACCESS REQUEST CLASS
# =====================================================

class AccessRequest:
    def __init__(self, username, facility_name, date_str, start_hour, end_hour, purpose):
        self.id = f"AR-{datetime.now().strftime('%Y%m%d%H%M%S')}-{random.randint(100, 999)}"
        self.username = username
        self.facility_name = facility_name
        self.date = date_str
        self.start_hour = start_hour
        self.end_hour = end_hour
        self.purpose = purpose
        self.status = "Pending"
        self.timestamp = datetime.now()
        self.encrypted_purpose = Cryptography.encrypt(purpose)
        self.actual_start_time = None
        self.actual_end_time = None
        self.time_used = None
    
    def to_dict(self):
        return {
            "id": self.id,
            "username": self.username,
            "facility": self.facility_name,
            "date": self.date,
            "time": f"{self.start_hour}:00 - {self.end_hour}:00",
            "purpose": self.purpose,
            "status": self.status,
            "encrypted_purpose": self.encrypted_purpose
        }

# =====================================================
# ROOM USAGE TRACKING
# =====================================================

class RoomUsage:
    """Track room usage with time allotment"""
    
    def __init__(self, room_name, user, start_time, end_time, duration_minutes=60):
        self.room_name = room_name
        self.user = user
        self.start_time = start_time
        self.end_time = end_time
        self.duration_minutes = duration_minutes
        self.is_active = True
        self.actual_end_time = None
    
    def get_remaining_minutes(self):
        """Get remaining minutes for this usage"""
        if not self.is_active:
            return 0
        now = datetime.now()
        if now >= self.end_time:
            return 0
        diff = self.end_time - now
        return int(diff.total_seconds() / 60)
    
    def is_available(self, requested_time):
        """Check if room is available at requested time"""
        if not self.is_active:
            return True
        if requested_time < self.start_time or requested_time > self.end_time:
            return True
        return False
    
    def end_usage(self):
        """End room usage"""
        self.is_active = False
        self.actual_end_time = datetime.now()
        return self.actual_end_time
    
    def to_dict(self):
        return {
            'room': self.room_name,
            'user': self.user,
            'start_time': self.start_time.strftime('%Y-%m-%d %H:%M'),
            'end_time': self.end_time.strftime('%Y-%m-%d %H:%M'),
            'duration_minutes': self.duration_minutes,
            'is_active': self.is_active,
            'remaining_minutes': self.get_remaining_minutes()
        }

# =====================================================
# ROOM USAGE STORAGE
# =====================================================

room_usages = []

# =====================================================
# NOTIFICATION SYSTEM
# =====================================================

class Notification:
    """Notification system for access request updates"""
    
    def __init__(self, user_id, title, message, notification_type, request_id=None):
        self.id = f"NOTIF-{datetime.now().strftime('%Y%m%d%H%M%S')}-{random.randint(100, 999)}"
        self.user_id = user_id
        self.title = title
        self.message = message
        self.notification_type = notification_type  # 'approval', 'rejection', 'info', 'warning'
        self.request_id = request_id
        self.timestamp = datetime.now()
        self.is_read = False
    
    def mark_as_read(self):
        self.is_read = True
    
    def to_dict(self):
        return {
            'id': self.id,
            'user_id': self.user_id,
            'title': self.title,
            'message': self.message,
            'notification_type': self.notification_type,
            'request_id': self.request_id,
            'timestamp': self.timestamp.strftime('%Y-%m-%d %H:%M:%S'),
            'is_read': self.is_read,
            'time_ago': self.get_time_ago()
        }
    
    def get_time_ago(self):
        """Get time ago string"""
        diff = datetime.now() - self.timestamp
        seconds = diff.total_seconds()
        
        if seconds < 60:
            return f"{int(seconds)} seconds ago"
        elif seconds < 3600:
            return f"{int(seconds / 60)} minutes ago"
        elif seconds < 86400:
            return f"{int(seconds / 3600)} hours ago"
        else:
            return f"{int(seconds / 86400)} days ago"

# =====================================================
# NOTIFICATION STORAGE
# =====================================================

notifications = []

# =====================================================
# NOTIFICATION FUNCTIONS
# =====================================================

def create_notification(username, title, message, notification_type, request_id=None):
    """Create and store a notification for a user"""
    notif = Notification(username, title, message, notification_type, request_id)
    notifications.append(notif)
    return notif

def get_user_notifications(username):
    """Get all notifications for a user"""
    return [n for n in notifications if n.user_id == username]

def get_unread_notifications(username):
    """Get unread notifications for a user"""
    return [n for n in notifications if n.user_id == username and not n.is_read]

def mark_notification_read(notification_id):
    """Mark a notification as read"""
    for n in notifications:
        if n.id == notification_id:
            n.mark_as_read()
            return True
    return False

def mark_all_notifications_read(username):
    """Mark all notifications as read for a user"""
    count = 0
    for n in notifications:
        if n.user_id == username and not n.is_read:
            n.mark_as_read()
            count += 1
    return count

def get_notification_count(username):
    """Get unread notification count for a user"""
    return len(get_unread_notifications(username))

# =====================================================
# ACCESS LOGIC WITH USER CLASSIFICATION
# =====================================================

class AccessLogic:
    @staticmethod
    def can_access(user, facility_name):
        """Check if user can access a facility based on their classification"""
        if not user:
            return False
        
        # Check for Authorized User
        if user.user_type == "Authorized":
            if facility_name in user.authorized_rooms:
                return True
            return False
        
        # Check for Restricted User
        if user.user_type == "Restricted":
            if facility_name in user.restricted_rooms:
                return True
            return False
        
        # Check for Visitor
        if user.user_type == "Visitor":
            public_areas = ["LIBRARY", "STUDENT ACTIVITY CENTER", "ADMIN OFFICE", "MAIN GATE"]
            if facility_name in public_areas:
                return True
            return False
        
        # Standard users (Faculty, Staff, Chairperson, Student)
        if user.role in ["Faculty", "Chairperson"]:
            if facility_name in ["LIBRARY", "COMLAB 1", "COMLAB 2", "COMLAB 3", "COMLAB 4", "S&T LAB 1", "S&T LAB 2", "FACULTY OFFICE"]:
                return True
        
        if user.role == "Staff":
            if facility_name in ["LIBRARY", "CSM OFFICE"]:
                return True
        
        if user.role == "Student":
            for req in access_requests:
                if req.username == user.username and req.facility_name == facility_name and req.status == "Approved":
                    return True
            if user.program:
                room_program = ROOM_PROGRAM_MAPPING.get(facility_name, 'General')
                if room_program == user.program:
                    return True
        
        return False
    
    @staticmethod
    def can_request_access(user):
        """Check if user can request access"""
        if user.user_type in ["Restricted", "Visitor"]:
            return False
        return user.role in ["Student", "Faculty", "Staff", "Chairperson"]
    
    @staticmethod
    def evaluate_boolean_access(role, user_type="Standard", has_request=False, request_approved=False):
        """Evaluate access based on role and user type"""
        is_faculty = role == "Faculty"
        is_chair = role == "Chairperson"
        is_staff = role == "Staff"
        is_student = role == "Student"
        is_visitor = user_type == "Visitor"
        is_authorized = user_type == "Authorized"
        is_restricted = user_type == "Restricted"
        
        if is_restricted:
            return False
        if is_visitor:
            return False
        if is_authorized:
            return True
        
        access = is_faculty or is_chair or is_staff or (is_student and has_request and request_approved)
        return bool(access)
    
    @staticmethod
    def get_room_availability(room_name, current_time=None):
        """Check if a room is currently available"""
        if current_time is None:
            current_time = datetime.now()
        
        for usage in room_usages:
            if usage.room_name == room_name and usage.is_active:
                if usage.start_time <= current_time <= usage.end_time:
                    return {
                        'available': False,
                        'occupied_by': usage.user,
                        'until': usage.end_time
                    }
        
        return {
            'available': True,
            'occupied_by': None,
            'until': None
        }
    
    @staticmethod
    def assign_room_time(room_name, user, duration_minutes=60):
        """Assign time allotment for room usage"""
        current_time = datetime.now()
        end_time = current_time + timedelta(minutes=duration_minutes)
        
        usage = RoomUsage(room_name, user, current_time, end_time, duration_minutes)
        room_usages.append(usage)
        return usage

# =====================================================
# CAN ACCESS ROOM BY PROGRAM
# =====================================================

def can_access_room(user, room_name):
    """Check if user can access a room based on their program and classification"""
    if not user:
        return False
    
    if user.user_type == "Authorized":
        return room_name in user.authorized_rooms
    
    if user.user_type == "Restricted":
        return room_name in user.restricted_rooms
    
    if user.user_type == "Visitor":
        public_areas = ["LIBRARY", "STUDENT ACTIVITY CENTER", "ADMIN OFFICE", "MAIN GATE"]
        return room_name in public_areas
    
    if user.role in ['Faculty', 'Staff']:
        return True
    
    if user.role == 'Chairperson':
        room_program = ROOM_PROGRAM_MAPPING.get(room_name, 'General')
        if user.chairperson_college == 'COLLEGE OF SCIENCE AND MANAGEMENT':
            if room_program in ['BSCS', 'BSES', 'BSHM', 'CSM']:
                return True
        elif user.chairperson_college == 'COLLEGE OF TEACHER EDUCATION':
            if room_program in ['BEED', 'BSED-MATH', 'BTLED-HE', 'CTE']:
                return True
        return False
    
    if user.role == 'Student':
        room_program = ROOM_PROGRAM_MAPPING.get(room_name, 'General')
        if room_program == user.program:
            return True
        for req in access_requests:
            if req.username == user.username and req.facility_name == room_name and req.status == 'Approved':
                return True
        return False
    
    return False

# =====================================================
# REGISTRATION FUNCTION
# =====================================================

def register_user(school_id, username, password, role, full_name, program="", user_type="Standard", authorized_rooms=None, restricted_rooms=None):
    for user in users:
        if user.school_id == school_id:
            return False, "School ID already exists"
        if user.username == username:
            return False, "Username already exists"
    
    valid_roles = ["Student", "Faculty", "Staff", "Chairperson", "Visitor"]
    if role not in valid_roles:
        return False, f"Invalid role. Choose from: {', '.join(valid_roles)}"
    
    new_user = User(school_id, username, password, role, full_name, program, authorized_rooms, restricted_rooms)
    new_user.user_type = user_type
    users.append(new_user)
    
    if role == "Student":
        students.add(username)
    elif role == "Faculty":
        faculty.add(username)
    elif role == "Staff":
        staff.add(username)
    elif role == "Chairperson":
        chairpersons.add(username)
    elif role == "Visitor":
        visitors.add(username)
    
    if user_type == "Authorized":
        authorized_users.add(username)
    elif user_type == "Restricted":
        restricted_users.add(username)
    
    return True, "User registered successfully"

# =====================================================
# ACCESS CHECKING FUNCTION
# =====================================================

def check_access(username, facility_name, duration_minutes=60):
    """Check access and assign time allotment if granted"""
    user = None
    for u in users:
        if u.username == username:
            user = u
            break
    
    if not user:
        return False, "User not found", None
    
    if facility_name not in facilities_set:
        return False, "Facility does not exist", None
    
    if user.user_type == "Restricted":
        if facility_name not in user.restricted_rooms:
            return False, "Access Denied: Restricted user cannot access this facility", None
    
    if user.user_type == "Authorized":
        if facility_name not in user.authorized_rooms:
            return False, "Access Denied: This facility is not in your authorized list", None
    
    if user.user_type == "Visitor":
        public_areas = ["LIBRARY", "STUDENT ACTIVITY CENTER", "ADMIN OFFICE", "MAIN GATE"]
        if facility_name not in public_areas:
            return False, "Access Denied: Visitors can only access public areas", None
    
    row = role_to_row.get(user.role)
    col = facility_to_col.get(facility_name)
    
    if row is None or col is None:
        return False, "Invalid role or facility", None
    
    matrix_permission = access_matrix[row][col]
    
    availability = AccessLogic.get_room_availability(facility_name)
    if not availability['available']:
        return False, f"Room is occupied by {availability['occupied_by']} until {availability['until'].strftime('%H:%M')}", None
    
    if user.role in ["Faculty", "Chairperson", "Staff"]:
        authorized = matrix_permission == 1
    elif user.role == "Student":
        has_approved = False
        for req in access_requests:
            if req.username == username and req.facility_name == facility_name and req.status == "Approved":
                has_approved = True
                break
        authorized = matrix_permission == 1 and has_approved
    else:
        authorized = matrix_permission == 1
    
    if authorized:
        user.is_authorized = True
        user.access_count += 1
        fsm.transition(FiniteStateMachine.STATES['ACCESS_GRANTED'])
        
        usage = AccessLogic.assign_room_time(facility_name, username, duration_minutes)
        return True, f"Access Granted. You have {duration_minutes} minutes.", usage
    else:
        fsm.transition(FiniteStateMachine.STATES['ACCESS_DENIED'])
        return False, "Access Denied", None

# =====================================================
# NUMBER THEORY FUNCTIONS
# =====================================================

def verify_id(school_id):
    try:
        parts = school_id.split('-')
        if len(parts) != 2:
            return False, "Invalid ID format. Use YYYY-XXXX format"
        
        year = int(parts[0])
        number = int(parts[1])
        
        if year != 2026:
            return False, "Invalid school year"
        
        if number % 2 != 0:
            return False, "ID number must be even (modular arithmetic check)"
        
        for user in users:
            if user.school_id == school_id:
                return True, "Valid ID found"
        
        return False, "ID not found in system"
        
    except ValueError:
        return False, "Invalid ID format"

def calculate_priority_score(username, facility_name):
    name_sum = sum(ord(c) for c in username)
    facility_sum = sum(ord(c) for c in facility_name)
    gcd_value = math.gcd(name_sum, facility_sum)
    return gcd_value

def get_time_slot_hash(date_str, start_hour, facility_name):
    date_hash = sum(ord(c) for c in date_str)
    time_hash = (start_hour * 60) % 24
    facility_hash = sum(ord(c) for c in facility_name) % 10
    total_hash = (date_hash * time_hash + facility_hash) % 100
    return total_hash

# =====================================================
# ENCRYPTED MESSAGE FUNCTIONS
# =====================================================

def encrypt_message(message):
    return Cryptography.encrypt(message)

def decrypt_message(encrypted):
    return Cryptography.decrypt(encrypted)

# =====================================================
# INITIALIZE SYSTEM
# =====================================================

def initialize_system():
    for user_data in USER_DATA:
        register_user(
            user_data["school_id"],
            user_data["username"],
            user_data["password"],
            user_data["role"],
            user_data["full_name"],
            user_data.get("program", ""),
            "Standard"
        )
        if user_data.get("role") == "Chairperson" and user_data.get("chairperson_college"):
            for u in users:
                if u.username == user_data["username"]:
                    u.chairperson_college = user_data["chairperson_college"]
                    break
    
    for visitor_data in VISITOR_DATA:
        register_user(
            visitor_data["school_id"],
            visitor_data["username"],
            visitor_data["password"],
            "Visitor",
            visitor_data["full_name"],
            "",
            "Visitor"
        )
    
    for auth_data in AUTHORIZED_USER_DATA:
        register_user(
            auth_data["school_id"],
            auth_data["username"],
            auth_data["password"],
            auth_data["role"],
            auth_data["full_name"],
            auth_data.get("program", ""),
            "Authorized",
            auth_data.get("authorized_rooms", [])
        )
    
    for rest_data in RESTRICTED_USER_DATA:
        register_user(
            rest_data["school_id"],
            rest_data["username"],
            rest_data["password"],
            rest_data["role"],
            rest_data["full_name"],
            rest_data.get("program", ""),
            "Restricted",
            None,
            rest_data.get("restricted_rooms", [])
        )
    
    global fsm
    fsm = FiniteStateMachine()

# =====================================================
# FLASK WEB ROUTES
# =====================================================

@app.route('/')
def home():
    if 'username' in session:
        return redirect(url_for('dashboard'))
    return redirect(url_for('login'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username', '').strip()
        password = request.form.get('password', '').strip()
        
        if not username or not password:
            flash('Please enter both username and password', 'error')
            return render_template('login.html', datetime=datetime)
        
        fsm.transition(FiniteStateMachine.STATES['LOGIN'])
        
        user = None
        for u in users:
            if u.username == username:
                user = u
                break
        
        if user and user.verify_password(password):
            session['username'] = user.username
            session['user_type'] = user.role
            session['full_name'] = user.full_name
            session['user_classification'] = user.user_type
            flash(f'Welcome back, {user.full_name}!', 'success')
            fsm.transition(FiniteStateMachine.STATES['ACCESS_GRANTED'])
            return redirect(url_for('dashboard'))
        else:
            flash('Invalid username or password', 'error')
            fsm.transition(FiniteStateMachine.STATES['ACCESS_DENIED'])
    
    return render_template('login.html', datetime=datetime)

@app.context_processor
def utility_processor():
    from datetime import datetime
    return {
        'fsm_states': FiniteStateMachine.STATES,
        'get_fsm_state': lambda: fsm.get_state(),
        'datetime': datetime,
        'get_notification_count': lambda username=None: get_notification_count(username) if username else 0,
        'get_unread_notifications': lambda username=None: get_unread_notifications(username) if username else []
    }

@app.route('/dashboard')
def dashboard():
    if 'username' not in session:
        return redirect(url_for('login'))
    
    user = None
    for u in users:
        if u.username == session['username']:
            user = u
            break
    
    user_data = {
        'full_name': user.full_name if user else 'Unknown',
        'school_id': user.school_id if user else 'N/A',
        'username': user.username if user else 'N/A',
        'password': user.password if user else 'N/A',
        'role': user.role if user else 'N/A',
        'program': user.program if user else 'N/A',
        'chairperson_college': user.chairperson_college if user else 'N/A',
        'access_count': user.access_count if user else 0,
        'user_type': user.user_type if user else 'Standard',
        'authorized_rooms': user.authorized_rooms if user else [],
        'restricted_rooms': user.restricted_rooms if user else []
    }
    
    room_status = []
    for room in ROOM_DATA:
        availability = AccessLogic.get_room_availability(room['room_name'])
        can_access = can_access_room(user, room['room_name']) if user else False
        program = ROOM_PROGRAM_MAPPING.get(room['room_name'], 'General')
        
        room_status.append({
            'room_id': room['room_id'],
            'room_name': room['room_name'],
            'room_number': room['room_number'],
            'type': room['type'],
            'program': program,
            'available': availability['available'],
            'occupied_by': availability['occupied_by'] if not availability['available'] else None,
            'until': availability['until'] if not availability['available'] else None,
            'can_access': can_access,
            'time_allotted': '60 minutes' if can_access else 'N/A'
        })
    
    active_usages = [usage.to_dict() for usage in room_usages if usage.is_active]
    user_requests = [req for req in access_requests if req.username == session['username']]
    
    return render_template('dashboard.html',
                         username=session['username'],
                         full_name=session.get('full_name', ''),
                         user_type=user.role if user else 'Unknown',
                         user_classification=user.user_type if user else 'Standard',
                         total_users=len(users),
                         total_requests=len(access_requests),
                         pending_requests=len([r for r in access_requests if r.status == 'Pending']),
                         requests=user_requests,
                         fsm_state=fsm.get_state(),
                         availability_probability=ProbabilityCalculator.room_availability_probability(
                             len(ROOM_DATA), 
                             len([r for r in access_requests if r.status == 'Approved'])
                         ),
                         room_status=room_status,
                         active_usages=active_usages,
                         user_data=user_data)

@app.route('/logout_confirm')
def logout_confirm():
    if 'username' not in session:
        return redirect(url_for('login'))
    return render_template('logout_confirm.html')

@app.route('/logout_do', methods=['POST'])
def logout_do():
    if 'username' not in session:
        return redirect(url_for('login'))
    fsm.transition(FiniteStateMachine.STATES['EXIT'])
    session.clear()
    flash('Logged out successfully', 'success')
    fsm.reset()
    return redirect(url_for('login'))

@app.route('/logout')
def logout():
    fsm.transition(FiniteStateMachine.STATES['EXIT'])
    session.clear()
    flash('Logged out successfully', 'success')
    fsm.reset()
    return redirect(url_for('login'))

@app.route('/check_access', methods=['GET', 'POST'])
def check_access_web():
    if 'username' not in session:
        return redirect(url_for('login'))
    
    result = None
    usage_info = None
    selected_facility = request.args.get('facility', '')
    
    if request.method == 'POST':
        facility = request.form.get('facility')
        duration = int(request.form.get('duration', 60))
        
        granted, message, usage = check_access(session['username'], facility, duration)
        
        result = {
            'granted': granted,
            'message': message,
            'facility': facility,
            'fsm_state': fsm.get_state()
        }
        
        if usage:
            usage_info = usage.to_dict()
    
    return render_template('check_access.html', 
                         facilities=facilities_set,
                         result=result,
                         usage_info=usage_info,
                         selected_facility=selected_facility,
                         fsm_state=fsm.get_state())

@app.route('/verify_id', methods=['GET', 'POST'])
def verify_id_web():
    if 'username' not in session:
        return redirect(url_for('login'))
    
    result = None
    if request.method == 'POST':
        school_id = request.form.get('school_id')
        valid, message = verify_id(school_id)
        result = {
            'valid': valid,
            'message': message,
            'school_id': school_id
        }
    
    return render_template('verify_id.html', result=result)

@app.route('/request_access', methods=['GET', 'POST'])
def request_access_web():
    if 'username' not in session:
        return redirect(url_for('login'))
    
    user = None
    for u in users:
        if u.username == session['username']:
            user = u
            break
    
    if not AccessLogic.can_request_access(user):
        flash('Your user type does not allow access requests', 'error')
        return redirect(url_for('dashboard'))
    
    all_facilities = []
    for room in ROOM_DATA:
        if room['room_name'] not in all_facilities:
            all_facilities.append(room['room_name'])
    
    if request.method == 'POST':
        facility = request.form.get('facility')
        date_str = request.form.get('date')
        start_hour = int(request.form.get('start_hour'))
        end_hour = int(request.form.get('end_hour'))
        purpose = request.form.get('purpose')
        
        if start_hour >= end_hour:
            flash('End time must be after start time', 'error')
            return render_template('request_access.html', facilities=all_facilities)
        
        req = AccessRequest(session['username'], facility, date_str, start_hour, end_hour, purpose)
        access_requests.append(req)
        flash(f'Request submitted! ID: {req.id}', 'success')
        return redirect(url_for('dashboard'))
    
    return render_template('request_access.html', facilities=all_facilities)

@app.route('/admin')
def admin():
    if 'username' not in session:
        return redirect(url_for('login'))
    
    user = None
    for u in users:
        if u.username == session['username']:
            user = u
            break
    
    if user and user.role not in ['Faculty', 'Chairperson', 'Staff']:
        flash('Admin access required', 'error')
        return redirect(url_for('dashboard'))
    
    pending = [req for req in access_requests if req.status == 'Pending']
    approved = [req for req in access_requests if req.status == 'Approved']
    
    approved_by_program = {}
    for req in approved:
        req_user = None
        for u in users:
            if u.username == req.username:
                req_user = u
                break
        program = req_user.program if req_user and req_user.program else 'General'
        if program not in approved_by_program:
            approved_by_program[program] = {'count': 0, 'users': []}
        approved_by_program[program]['count'] += 1
        if req_user and req_user.username not in approved_by_program[program]['users']:
            approved_by_program[program]['users'].append(req_user.username)
    
    room_usage_by_program = []
    for room in ROOM_DATA:
        availability = AccessLogic.get_room_availability(room['room_name'])
        program = ROOM_PROGRAM_MAPPING.get(room['room_name'], 'General')
        room_usage_by_program.append({
            'room_name': room['room_name'],
            'room_number': room['room_number'],
            'program': program,
            'available': availability['available'],
            'occupied_by': availability['occupied_by'] if not availability['available'] else None
        })
    
    user_stats = {
        'standard_users': len([u for u in users if u.user_type == 'Standard']),
        'authorized_users': len([u for u in users if u.user_type == 'Authorized']),
        'restricted_users': len([u for u in users if u.user_type == 'Restricted']),
        'visitors': len([u for u in users if u.user_type == 'Visitor']),
    }
    
    return render_template('admin.html',
                         pending_requests=pending,
                         total_users=len(users),
                         pending_requests_count=len(pending),
                         approved_requests=len(approved),
                         total_rooms=len(ROOM_DATA),
                         approved_by_program=approved_by_program,
                         room_usage_by_program=room_usage_by_program,
                         all_users=users,
                         user_stats=user_stats)
    
@app.route('/admin/approve/<request_id>')
def approve_request(request_id):
    if 'username' not in session:
        return redirect(url_for('login'))
    
    for req in access_requests:
        if req.id == request_id and req.status == 'Pending':
            req.status = 'Approved'
            access_history.append(req)
            
            for user in users:
                if user.username == req.username and user.role == 'Student':
                    row = role_to_row.get('Student')
                    col = facility_to_col.get(req.facility_name)
                    if row is not None and col is not None:
                        access_matrix[row][col] = 1
            
            create_notification(
                req.username,
                "✅ Access Request Approved",
                f"Your access request for {req.facility_name} on {req.date} has been APPROVED. You now have access to this facility.",
                "approval",
                req.id
            )
            
            flash(f'Request {request_id} approved!', 'success')
            break
    else:
        flash('Request not found', 'error')
    
    return redirect(url_for('admin'))

@app.route('/admin/reject/<request_id>')
def reject_request(request_id):
    if 'username' not in session:
        return redirect(url_for('login'))
    
    for req in access_requests:
        if req.id == request_id and req.status == 'Pending':
            req.status = 'Rejected'
            access_history.append(req)
            
            create_notification(
                req.username,
                "❌ Access Request Rejected",
                f"Your access request for {req.facility_name} on {req.date} has been REJECTED. Please contact the admin for more details.",
                "rejection",
                req.id
            )
            
            flash(f'Request {request_id} rejected', 'info')
            break
    else:
        flash('Request not found', 'error')
    
    return redirect(url_for('admin'))

# =====================================================
# REGISTER ROUTE
# =====================================================

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        full_name = request.form.get('full_name')
        school_id = request.form.get('school_id')
        username = request.form.get('username')
        password = request.form.get('password')
        role = request.form.get('role')
        program = request.form.get('program', '')
        chairperson_college = request.form.get('chairperson_college', '')
        user_type = request.form.get('user_type', 'Standard')
        
        if not full_name or not school_id or not username or not password or not role:
            flash('All fields are required', 'error')
            return render_template('register.html', 
                                 program_options=PROGRAM_OPTIONS,
                                 selected_role=role,
                                 selected_program=program,
                                 selected_user_type=user_type,
                                 form_data=request.form)
        
        for user in users:
            if user.school_id == school_id:
                flash('School ID already exists', 'error')
                return render_template('register.html', program_options=PROGRAM_OPTIONS)
            if user.username == username:
                flash('Username already exists', 'error')
                return render_template('register.html', program_options=PROGRAM_OPTIONS)
        
        if role == 'Student' and not program:
            flash('Program is required for students', 'error')
            return render_template('register.html', program_options=PROGRAM_OPTIONS)
        
        if role == 'Chairperson' and not chairperson_college:
            flash('College oversight is required for Chairperson', 'error')
            return render_template('register.html', program_options=PROGRAM_OPTIONS)
        
        new_user = User(school_id, username, password, role, full_name, program)
        new_user.user_type = user_type
        new_user.chairperson_college = chairperson_college if role == 'Chairperson' else ''
        users.append(new_user)
        
        if role == "Student":
            students.add(username)
        elif role == "Faculty":
            faculty.add(username)
        elif role == "Staff":
            staff.add(username)
        elif role == "Chairperson":
            chairpersons.add(username)
        elif role == "Visitor":
            visitors.add(username)
        
        if user_type == "Authorized":
            authorized_users.add(username)
        elif user_type == "Restricted":
            restricted_users.add(username)
        
        flash('User registered successfully!', 'success')
        return redirect(url_for('login'))
    
    return render_template('register.html', program_options=PROGRAM_OPTIONS)

# =====================================================
# NEW ROUTES
# =====================================================

@app.route('/navigation')
def navigation():
    if 'username' not in session:
        return redirect(url_for('login'))
    
    fsm.transition(FiniteStateMachine.STATES['NAVIGATING'])
    
    locations = campus_graph.get_locations()
    return render_template('navigation.html', 
                         locations=locations,
                         fsm_state=fsm.get_state())

@app.route('/find_route', methods=['POST'])
def find_route():
    if 'username' not in session:
        return redirect(url_for('login'))
    
    start = request.form.get('start')
    end = request.form.get('end')
    
    if start and end:
        result = campus_graph.find_shortest_path(start, end)
        all_paths = RecursiveFunctions.find_all_paths(campus_graph.adjacency_list, start, end)
        
        return render_template('route_result.html',
                             result=result,
                             all_paths=all_paths[:10],
                             start=start,
                             end=end,
                             fsm_state=fsm.get_state())
    
    return redirect(url_for('navigation'))

@app.route('/encrypt', methods=['GET', 'POST'])
def encrypt_message_web():
    if 'username' not in session:
        return redirect(url_for('login'))
    
    result = None
    if request.method == 'POST':
        message = request.form.get('message')
        action = request.form.get('action')
        
        if action == 'encrypt':
            result = {
                'original': message,
                'result': Cryptography.encrypt(message),
                'action': 'encrypted'
            }
        elif action == 'decrypt':
            result = {
                'original': message,
                'result': Cryptography.decrypt(message),
                'action': 'decrypted'
            }
    
    return render_template('encrypt.html', result=result)

@app.route('/campus_tree')
def campus_tree_view():
    if 'username' not in session:
        return redirect(url_for('login'))
    
    return render_template('campus_tree.html',
                         tree_data=campus_tree.root.to_dict(),
                         departments=campus_tree.get_departments(),
                         all_rooms=campus_tree.get_rooms(),
                         preorder=campus_tree.traverse_preorder(),
                         postorder=campus_tree.traverse_postorder())

@app.route('/fsm_status')
def fsm_status():
    if 'username' not in session:
        return redirect(url_for('login'))
    
    return render_template('fsm_status.html',
                         current_state=fsm.get_state(),
                         history=fsm.get_history(),
                         all_states=FiniteStateMachine.STATES)

@app.route('/probability_stats')
def probability_stats():
    if 'username' not in session:
        return redirect(url_for('login'))
    
    total_rooms = len(ROOM_DATA)
    occupied_rooms = len([r for r in access_requests if r.status == 'Approved'])
    
    total_attempts = sum(u.access_count for u in users)
    successful_attempts = len([r for r in access_requests if r.status == 'Approved'])
    
    all_paths = RecursiveFunctions.find_all_paths(campus_graph.adjacency_list, 'Main Gate', 'Library')
    
    room_sim = RandomVariables.simulate_room_availability(total_rooms)
    waiting_times = RandomVariables.generate_waiting_times(10)
    arrivals = RandomVariables.simulate_user_arrival(rate=3, time_period=30)
    
    stats = {
        'room_availability': ProbabilityCalculator.room_availability_probability(total_rooms, occupied_rooms),
        'access_success': ProbabilityCalculator.access_success_probability(total_attempts, successful_attempts),
        'route_options': ProbabilityCalculator.route_options_probability(max(len(campus_graph.adjacency_list), 1), len(all_paths)),
        'permutations_5_3': ProbabilityCalculator.permutation(5, 3),
        'combinations_5_3': RecursiveFunctions.combinations(5, 3),
        'factorial_5': RecursiveFunctions.factorial(5),
        'room_simulation': room_sim,
        'waiting_times': waiting_times,
        'simulated_arrivals': arrivals,
        'total_users': len(users),
        'total_requests': len(access_requests)
    }
    
    return render_template('probability_stats.html', stats=stats)

@app.route('/secure_messages')
def secure_messages():
    if 'username' not in session:
        return redirect(url_for('login'))
    
    messages = []
    for req in access_requests:
        messages.append({
            'user': req.username,
            'facility': req.facility_name,
            'encrypted': req.encrypted_purpose,
            'decrypted': req.purpose,
            'status': req.status
        })
    
    return render_template('secure_messages.html', messages=messages[:20])

@app.route('/user_profile')
def user_profile():
    if 'username' not in session:
        return redirect(url_for('login'))
    
    user = None
    for u in users:
        if u.username == session['username']:
            user = u
            break
    
    if not user:
        flash('User not found', 'error')
        return redirect(url_for('logout'))
    
    return render_template('user_profile.html',
                         user=user,
                         fsm_state=fsm.get_state())

@app.route('/rooms_facilities')
def rooms_facilities():
    if 'username' not in session:
        return redirect(url_for('login'))
    
    user = None
    for u in users:
        if u.username == session['username']:
            user = u
            break
    
    room_status = []
    for room in ROOM_DATA:
        availability = AccessLogic.get_room_availability(room['room_name'])
        can_access = can_access_room(user, room['room_name']) if user else False
        program = ROOM_PROGRAM_MAPPING.get(room['room_name'], 'General')
        
        has_approved_request = False
        if user:
            for req in access_requests:
                if req.username == user.username and req.facility_name == room['room_name'] and req.status == 'Approved':
                    has_approved_request = True
                    break
        
        access_reason = "No Access"
        if can_access:
            if user.user_type == "Authorized":
                access_reason = "Authorized User"
            elif user.user_type == "Restricted":
                access_reason = "Restricted Access"
            elif user.user_type == "Visitor":
                access_reason = "Public Area"
            elif user.role in ["Faculty", "Staff", "Chairperson"]:
                access_reason = "Staff/Faculty Access"
            elif user.role == "Student" and has_approved_request:
                access_reason = "Approved Request"
            else:
                access_reason = "Program Access"
        
        room_status.append({
            'room_id': room['room_id'],
            'room_name': room['room_name'],
            'room_number': room['room_number'],
            'type': room['type'],
            'program': program,
            'available': availability['available'],
            'occupied_by': availability['occupied_by'] if not availability['available'] else None,
            'until': availability['until'] if not availability['available'] else None,
            'can_access': can_access,
            'access_reason': access_reason,
            'has_approved_request': has_approved_request,
            'time_allotted': '60 minutes' if can_access else 'N/A'
        })
    
    classification_summary = {
        'standard_count': len([u for u in users if u.user_type == 'Standard']),
        'authorized_count': len([u for u in users if u.user_type == 'Authorized']),
        'restricted_count': len([u for u in users if u.user_type == 'Restricted']),
        'visitor_count': len([u for u in users if u.user_type == 'Visitor']),
    }
    
    return render_template('rooms_facilities.html',
                         room_status=room_status,
                         classification_summary=classification_summary,
                         fsm_state=fsm.get_state())

@app.route('/room_usage')
def room_usage_view():
    if 'username' not in session:
        return redirect(url_for('login'))
    
    user = None
    for u in users:
        if u.username == session['username']:
            user = u
            break
    
    active_usages = []
    all_usages = []
    user_active_usages = []
    
    for usage in room_usages:
        usage_dict = usage.to_dict()
        all_usages.append(usage_dict)
        
        if usage.is_active:
            active_usages.append(usage_dict)
            if usage.user == user.username:
                user_active_usages.append(usage_dict)
    
    return render_template('room_usage.html',
                         active_usages=active_usages,
                         all_usages=all_usages,
                         user_active_usages=user_active_usages,
                         fsm_state=fsm.get_state())

@app.route('/end_usage/<int:usage_index>')
def end_usage(usage_index):
    if 'username' not in session:
        return redirect(url_for('login'))
    
    if 0 <= usage_index < len(room_usages):
        usage = room_usages[usage_index]
        if usage.user == session['username'] or session.get('user_type') in ['Faculty', 'Chairperson', 'Staff']:
            end_time = usage.end_usage()
            flash(f'Room {usage.room_name} usage ended at {end_time.strftime("%H:%M")}', 'success')
        else:
            flash('You are not authorized to end this usage', 'error')
    else:
        flash('Usage record not found', 'error')
    
    return redirect(url_for('room_usage_view'))

# =====================================================
# NOTIFICATION ROUTES
# =====================================================

@app.route('/notifications')
def view_notifications():
    """View all notifications for the current user"""
    if 'username' not in session:
        return redirect(url_for('login'))
    
    user_notifs = get_user_notifications(session['username'])
    unread_count = get_notification_count(session['username'])
    
    return render_template('notifications.html',
                         notifications=user_notifs,
                         unread_count=unread_count,
                         fsm_state=fsm.get_state())

@app.route('/notifications/mark_read/<notification_id>')
def mark_notification_read_route(notification_id):
    """Mark a single notification as read"""
    if 'username' not in session:
        return redirect(url_for('login'))
    
    mark_notification_read(notification_id)
    return redirect(url_for('view_notifications'))

@app.route('/notifications/mark_all_read')
def mark_all_notifications_read_route():
    """Mark all notifications as read for the current user"""
    if 'username' not in session:
        return redirect(url_for('login'))
    
    count = mark_all_notifications_read(session['username'])
    flash(f'Marked {count} notifications as read', 'success')
    return redirect(url_for('view_notifications'))

@app.route('/notifications/unread_count')
def get_unread_count():
    """Get unread notification count (AJAX endpoint)"""
    if 'username' not in session:
        return jsonify({'count': 0})
    
    count = get_notification_count(session['username'])
    return jsonify({'count': count})

# =====================================================
# RUN APPLICATION
# =====================================================

if __name__ == '__main__':
    initialize_system()
    app.run(debug=True, host='0.0.0.0', port=5000)