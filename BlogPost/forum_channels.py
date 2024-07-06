from .models import Channel

channels = {
    "Python": "A powerful, high-level programming language known for its easy readability and wide range of libraries.",
    "JavaScript": "A versatile language primarily used for web development to create interactive elements on websites.",
    "Java": "A popular, object-oriented programming language used in various applications, from mobile to enterprise-level systems.",
    "C++": "A general-purpose programming language with low-level memory manipulation features, widely used in game development and system/software applications.",
    "Ruby": "A dynamic, open-source programming language with a focus on simplicity and productivity, known for its elegant syntax.",
    "HTML/CSS": "The foundational technologies for building and designing web pages, with HTML providing structure and CSS handling the presentation.",
    "SQL": "A domain-specific language used for managing and manipulating relational databases.",
    "Machine Learning": "A field of artificial intelligence focused on developing algorithms that allow computers to learn and make predictions based on data.",
    "Data Science": "A multidisciplinary field that uses scientific methods, processes, algorithms, and systems to extract knowledge and insights from structured and unstructured data.",
    "DevOps": "A set of practices that combines software development (Dev) and IT operations (Ops) aimed at shortening the development lifecycle and providing continuous delivery with high software quality.",
    "Cybersecurity": "The practice of protecting systems, networks, and programs from digital attacks, theft, and damage.",
    "Cloud Computing": "The delivery of computing services—including servers, storage, databases, networking, software, and more—over the cloud (internet).",
    "Mobile Development": "The process of creating software applications that run on mobile devices, with popular platforms being iOS and Android.",
    "Blockchain": "A decentralized digital ledger technology used for securely recording transactions across many computers.",
    "Artificial Intelligence": "The simulation of human intelligence processes by machines, especially computer systems.",
    "Front-end Development": "The practice of producing HTML, CSS, and JavaScript for a website or web application so that a user can see and interact with them directly.",
    "Back-end Development": "The server-side development that focuses on databases, scripting, and the architecture of websites.",
    "Full Stack Development": "Development that involves working on both the front-end and back-end of an application.",
    "Internet of Things (IoT)": "The network of physical objects that are embedded with sensors, software, and other technologies to connect and exchange data with other devices and systems over the internet.",
    "Game Development": "The art of creating games and describes the design, development, and release of a game.",
    "Big Data": "A field that treats ways to analyze, systematically extract information from, or otherwise deal with data sets that are too large or complex to be dealt with by traditional data-processing application software.",
    "Agile Development": "A set of principles for software development under which requirements and solutions evolve through the collaborative effort of self-organizing and cross-functional teams and their customer/end user.",
    "Software Testing": "The process of evaluating and verifying that a software application or program does what it is supposed to do.",
    "UX/UI Design": "The process of enhancing user satisfaction with a product by improving the usability, accessibility, and pleasure provided in the interaction with the product.",
    "API Development": "The process of building and maintaining the API (Application Programming Interface) for a software application.",
    "Serverless Computing": "A cloud-computing execution model in which the cloud provider dynamically manages the allocation and provisioning of servers.",
    "Containerization": "A lightweight form of virtualization that involves encapsulating an application and its dependencies into a container that can run on any computing environment.",
    "Web Assembly": "A binary instruction format for a stack-based virtual machine that is designed to be a portable compilation target for programming languages, enabling deployment on the web for client and server applications.",
    "Progressive Web Apps (PWA)": "A type of application software delivered through the web, built using common web technologies including HTML, CSS, and JavaScript, intended to work on any platform that uses a standards-compliant browser.",
    "Web Security": "Measures and protocols to protect websites and web applications from being attacked or compromised.",
    "Networking": "The practice of connecting computers and other devices together to share resources.",
    "Operating Systems": "The software that supports a computer's basic functions, such as scheduling tasks, executing applications, and controlling peripherals.",
    "Embedded Systems": "A computer system with a dedicated function within a larger mechanical or electrical system.",
    "Robotics": "The branch of technology that deals with the design, construction, operation, and application of robots.",
    "AR/VR Development": "The development of Augmented Reality (AR) and Virtual Reality (VR) applications.",
    "Functional Programming": "A programming paradigm where programs are constructed by applying and composing functions.",
    "Version Control": "The management of changes to documents, computer programs, large websites, and other collections of information.",
    'Spring Framework': 'A Java framework that provides comprehensive infrastructure support for developing Java applications.',
    'Ruby on Rails': 'A server-side web application framework written in Ruby under the MIT License. It is a model–view–controller (MVC) framework, providing default structures for a database, a web service, and web pages.',
    'Angular': 'A TypeScript-based open-source web application framework led by the Angular Team at Google and by a community of individuals and corporations.',
    'React': 'A JavaScript library for building user interfaces, maintained by Facebook and a community of individual developers and companies.',
    'Express.js': 'A minimal and flexible Node.js web application framework that provides a robust set of features for web and mobile applications.'
}


def create_channels():
    for name, description in channels.items():
        # Check if the channel already exists
        channel, created = Channel.objects.get_or_create(
            name=name, defaults={'description': description})

        if created:
            print(f"Created channel: {channel}")
        else:
            print(f"Channel '{channel}' already exists, skipping.")


if __name__ == '__main__':
    create_channels()
