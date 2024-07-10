# EduPool😎

## Created for COSC 310 course as a team project, but this branch has been modified as per personal direction by Rajveer Sodhi

The below text outlines the requirements for a canvas quiz like platform designed to facilitate interaction among administrators, students, and professors. The system aims to provide a seamless experience in course management, assignment distribution, and grading, alongside fostering an engaging community through a discussion portal.

## User Requirements

### Common Features
- **User Registration & Login:** Admin, students, and professors can sign up and log in with specific roles and permissions.

### Admin-Specific Features
- **Course Management:** Ability to create courses and approve student enrollments.
- **Professor Appointments:** Admins can assign professors to courses.

### Professor-Specific Features
- **Assignment Creation:** Professors can create various types of assignments, including quizzes and essays.
- **Grading & Insights:** Ability to grade assignments and quizzes, and view all students' grades.

### Student-Specific Features
- **Course Enrollment:** Students can enroll in courses of their choice.
- **Assignment Interaction:** Access to view and complete assignments and quizzes.
- **Grade Visibility:** Students can view their grades for each course.

### Community Interaction
- **Discussion Portal:** Both students and professors can create posts and reply to existing posts on the discussion portal.

## Functional Requirements

- **Authentication:** Secure user authentication during login.
- **Course Identification:** Unique identification for each course offering through department number, course number, and session/year code.
- **Personal Information Management:** Students can update personal details like address and major.
- **Deadline Enforcement:** System enforces assignment submission deadlines.
- **Quiz Management:** Instructors can create quizzes with various question types and settings.
- **Automatic Grading:** Objective assignments and quizzes are automatically graded.
- **Attempt Management:** Instructors can set rules around the number of attempts for quizzes and assignments.

## Non-functional Requirements

- **Performance:** The app must remain responsive and perform under heavy loads.
- **Efficiency:** Fast data processing and retrieval for minimal loading times.
- **Security:** Secure authentication and data encryption to protect user information.
- **Technology Stack:** Development using Python, Flask, and Bootstrap CSS.
- **Privacy:** Limited disclosure of student information to professors.
- **Data Protection:** Strong measures to prevent unauthorized access to user information.

This platform is designed to enhance the educational experience by streamlining administrative tasks, facilitating interactive learning, and ensuring a secure and efficient online environment for all users.
