import re
import random
from fuzzywuzzy import fuzz

class NLPChatbot:
    def generate_response(self, user_input):
        # Convert input to lowercase for easier matching
        user_input = re.sub(r'\s+', ' ', user_input.lower().strip())

        # Define keyword-response mappings
        keyword_responses = {
             ("hello", "hi", "hey", "greetings", "howdy"): ["Hello! How can I help you today?", "Hi there! What can I do for you?"],
            ("who are you", "your name", "what's your name", "introduce yourself", "about you"): ["I'm your friendly chatbot!", "You can call me Chatbot!"],
            ("how are you", "how do you do", "how's it going", "what's up", "how are things"): ["I'm just a bot, but I'm here to assist you!", "I'm doing well, thanks! How about you?"],
            
            ("created you", "who made you", "who built you", "who designed you", "your creator"): ["I was created by a team of developers.", "I’m the product of brilliant minds working with code and AI!", "A team of dedicated engineers and programmers brought me to life."],
            ("your purpose", "what's your purpose", "what do you do", "why are you here", "your goal"): ["My purpose is to assist you with your questions and tasks.", "I’m here to help, chat, and make your experience better!", "I exist to provide information and support whenever you need it."],
            ("how do I contact support", "contact support", "reach support", "support contact", "support information"): ["You can contact support by emailing us at support@example.com.", "Our support team is available at support@example.com.", "Feel free to reach out to our support team at support@example.com for assistance."],

            ("courses", "course offerings", "what courses do you offer", "list of courses", "available courses"): ["We offer various courses in Engineering, Arts, and Science. For details, please visit our website.", "Our college provides a wide range of programs in different fields. You can explore all courses on our website.", "Interested in our courses? Visit the courses section on our website for more information."],
            ("admission requirements", "requirements", "how to get admitted", "admission criteria", "admissions criteria"): ["Admission requirements vary by program. Please check the specific program's page on our website for details.", "Each program has its own set of admission criteria. You can find more information on our website's admissions page.", "For detailed admission requirements, please refer to the program-specific pages on our website."],
            ("application deadline", "deadline", "application date", "when is the deadline", "submit by"): ["The application deadlines vary. Check the admissions page on our website for the most accurate information.", "Don't miss the deadline! Visit our admissions page for the latest application dates.", "Application deadlines differ by program. Be sure to check the exact dates on our website."],
            ("location", "where are you located", "address", "college location", "where can I find you"): ["Our college is located at [Address]. You can find the exact location on our website's contact page.", "We're based at [Address]. For more details, please visit our contact page.", "You can find us at [Address]. Our website has a map and directions under the contact section."],
            ("online courses", "distance learning", "virtual courses", "e-learning", "online programs"): ["Yes, we offer a variety of online courses. Visit our website to see the full list of available online programs.", "Looking for online courses? We've got you covered! Check out the online programs on our website.", "We offer several online courses across different fields. More information is available on our website."],
            ("tuition fees", "cost", "how much is tuition", "tuition cost", "fees"): ["Tuition fees vary by program and residency status. You can find detailed information on our website.", "For specific tuition fee details, please visit the tuition and fees section on our website.", "Tuition fees depend on the program you choose. More information is available on our website."],
            ("scholarships", "financial aid", "scholarship opportunities", "scholarship programs", "aid"): ["We offer a variety of scholarships for eligible students. Visit our financial aid page for details.", "Looking for scholarships? Check out the scholarships section on our website for opportunities.", "Our college provides several scholarships based on merit and need. Find out more on our website."],
            ("campus life", "student activities", "life on campus", "campus events", "what's happening on campus"): ["Campus life at our college is vibrant and diverse. Learn more about student activities on our website.", "From clubs to events, there's always something happening on campus! Visit our campus life page for more.", "Explore the vibrant campus life at our college on the website's student life section."],
            ("how to apply", "application process", "applying", "submit application", "how to get started"): ["You can apply online through our admissions portal. Visit the 'Apply Now' section on our website.", "Applying is easy! Just head to our admissions page and follow the steps to apply online.", "Ready to join us? Visit the admissions page on our website and start your application process."],
            ("contact", "get in touch", "reach out", "contact us", "how to contact"): ["You can reach us via email or phone. Visit the contact page on our website for details.", "Need to get in touch? Our contact information is available on the website's contact section.", "For any inquiries, please visit our contact page for the best ways to reach us."],
            ("housing options", "student housing", "accommodation", "where to live", "housing facilities"): ["We offer a variety of housing options for students. Check out the housing section on our website.", "Looking for housing? Visit our website's housing page for details on available options.", "Our college provides several on-campus and off-campus housing options. More info is on our website."],
            ("student support services", "support services", "student help", "counseling services", "student assistance"): ["We offer a range of support services for students, including counseling and career guidance. Learn more on our website.", "Need support? Our student services are here to help. Visit our website for more information.", "Our college provides comprehensive support services to help you succeed. Details are on our website."],
            ("library hours", "library schedule", "when is the library open", "library timings", "hours of operation"): ["Our library hours vary during the semester. Check the library section on our website for current hours.", "Need to visit the library? Find the current hours on our website's library page.", "Library hours are updated regularly. Please visit our website for the latest schedule."],
            ("extracurricular activities", "clubs and societies", "student clubs", "activities", "what to do on campus"): ["We have a wide range of extracurricular activities, from sports to arts. Learn more on our website.", "Want to get involved? Explore the extracurricular activities we offer on our campus life page.", "There's something for everyone here! Check out our extracurricular activities on the website."],
            ("college name", "name of the college", "what is the college called", "college title", "college identity"): ["Our college is [College Name].", "You are inquiring about [College Name].", "We proudly represent [College Name]."],
            ("college details", "information about the college", "college info", "college overview", "what's the college about"): ["Our college, [College Name], offers a variety of programs and has a vibrant campus life. For detailed information about our courses, facilities, and more, please visit our website.", "You can learn more about [College Name], including our academic programs, campus facilities, and student life, on our official website.", "For comprehensive details about [College Name], including admissions, programs, and campus resources, please check out the information available on our website."],

            ("grades", "check grades", "view grades", "grade report", "how to see my grades"): ["You can check your grades by logging into your student portal and navigating to the grades section."],
            ("register for classes", "class registration", "sign up for classes", "course registration", "enroll in classes"): ["To register for classes, log into your student portal and follow the registration instructions under the 'Courses' tab."],
            ("student id", "student identification", "ID number", "unique student ID", "student identifier"): ["The student ID is a unique identifier assigned to each student. It typically consists of a combination of letters and numbers."],
            ("financial aid", "aid applications", "apply for financial aid", "financial assistance", "scholarship applications"): ["Financial aid applications can be submitted through the financial aid section of the student portal. Check our website for deadlines and required documents."],
            ("class schedule", "schedule", "view schedule", "course timetable", "class timings"): ["Your class schedule can be viewed in the student portal under the 'Schedule' tab."],

            ("facilities", "campus facilities", "on-campus amenities", "available facilities", "what's on campus"): ["We have a library, gym, cafeteria, and various recreational facilities on campus. For more details, visit our campus facilities page."],
            ("library", "library location", "where is the library", "library building", "find the library"): ["The library is located in Building A, near the main entrance."],
            ("campus map", "map", "campus layout", "where is the campus map", "find the campus map"): ["Yes, you can find the campus map on our website under the 'Campus Life' section."],

            ("clubs", "student clubs", "campus clubs", "club activities", "what clubs are available"): ["We have a variety of clubs and organizations, including sports teams, academic societies, and hobby clubs. Visit our student life page for more information."],
            ("join a club", "club membership", "how to join a club", "become a member", "sign up for a club"): ["To join a club, visit the club fair held at the beginning of each semester or contact the student activities office."],

            ("admissions office", "contact admissions", "reach admissions office", "admissions contact", "how to contact admissions"): ["You can contact the admissions office by phone at [Phone Number] or by email at [Email Address]."],
            ("office hours", "working hours", "business hours", "when is the office open", "office schedule"): ["Our office hours are Monday to Friday, 9 AM to 5 PM."],
            ("housing", "accommodation", "housing options", "student housing", "where to live"): ["Information about housing can be found on our website under the 'Housing' section."],

            ("feedback", "provide feedback", "give feedback", "submit feedback", "feedback form"): ["You can provide feedback through the feedback form available on our website or by contacting the student services office."],
            ("complaint", "file a complaint", "make a complaint", "submit a complaint", "complaint form"): ["To file a complaint, please contact the student affairs office or use the complaint form available on our website."],
            
        }

     # Exact match check first
        for keywords, responses in keyword_responses.items():
            if user_input in keywords:
                return random.choice(responses)

        # Fuzzy matching for partial or approximate matches
        for keywords, responses in keyword_responses.items():
            for keyword in keywords:
                if fuzz.partial_ratio(keyword, user_input) > 80:  # Adjust the ratio as needed
                    return random.choice(responses)
        return "Sorry, I didn't quite understand that. Could you please rephrase related to college information ?"