jobroles = [
    "Accountant",
    "Marketing Manager",
    "Corporate Counsel",
    "Account Manager",
    "Digital Marketer",
    "Product Development Manager",
    "Research Scientist",
    "Employee Relations Specialist",
    "Production Supervisor",
    "Supply Chain Manager",
    "Financial Controller",
    "Call Center Supervisor",
    "Brand Manager",
    "Public Relations Specialist",
    "Regulatory Affairs Specialist",
    "Training and Development Manager",
    "Database Administrator",
    "IT Manager",
    "Compliance Officer",
    "Quality Control Analyst",
    "Auditor",
    "Customer Support Specialist",
    "Tax Specialist",
    "Warehouse Manager",
    "Logistics Coordinator",
    "Systems Analyst",
    "Software Engineer",
    "Treasury Analyst",
    "Scrum Master",
    "Recruitment Specialist",
    "IT Support Specialist",
    "Compensation and Benefits Specialist",
    "Web Developer",
    "Customer Service Representative",
    "Market Research Analyst",
    "Financial Analyst",
    "HR Generalist",
    "Legal Assistant",
    "Cybersecurity Analyst",
    "Project Manager",
    "Network Administrator",
    "Team Lead",
    "Research Analyst",
    "Help Desk Analyst",
    "Innovation Manager",
    "Sales Representative",
    "Project Coordinator",
    "HR Manager",
    "Operations Manager",
    "CFO (Chief Financial Officer)",
    "CMO (Chief Marketing Officer)",
    "CTO (Chief Technology Officer)",
    "CEO (Chief Executive Officer)",
]

posts = [
    "Entry Level/Junior",
    "Associate/Specialist",
    "Mid-Level/Intermediate",
    "Senior/Lead",
    "Manager/Supervisor",
    "Director/Head",
    "Vice President/Executive",
]

departments = [
    "Finance and Accounting",
    "Sales and Marketing",
    "Legal and Compliance",
    "Research and Development (R&D)",
    "Human Resources (HR)",
    "Operations",
    "Customer Support",
    "Information Technology (IT)",
    "Quality Assurance (QA)",
    "Project Management",
    "Business Development",
]

jobrole_to_department = {
    "Accountant": "Finance and Accounting",
    "Marketing Manager": "Sales and Marketing",
    "Corporate Counsel": "Legal and Compliance",
    "Account Manager": "Sales and Marketing",
    "Digital Marketer": "Sales and Marketing",
    "Product Development Manager": "Research and Development (R&D)",
    "Research Scientist": "Research and Development (R&D)",
    "Employee Relations Specialist": "Human Resources (HR)",
    "Production Supervisor": "Operations",
    "Supply Chain Manager": "Operations",
    "Financial Controller": "Finance and Accounting",
    "Call Center Supervisor": "Customer Support",
    "Brand Manager": "Sales and Marketing",
    "Public Relations Specialist": "Sales and Marketing",
    "Regulatory Affairs Specialist": "Legal and Compliance",
    "Training and Development Manager": "Human Resources (HR)",
    "Database Administrator": "Information Technology (IT)",
    "IT Manager": "Information Technology (IT)",
    "Compliance Officer": "Legal and Compliance",
    "Quality Control Analyst": "Quality Assurance (QA)",
    "Auditor": "Finance and Accounting",
    "Customer Support Specialist": "Customer Support",
    "Tax Specialist": "Finance and Accounting",
    "Warehouse Manager": "Operations",
    "Logistics Coordinator": "Operations",
    "Systems Analyst": "Information Technology (IT)",
    "Software Engineer": "Information Technology (IT)",
    "Treasury Analyst": "Finance and Accounting",
    "Scrum Master": "Project Management",
    "Recruitment Specialist": "Human Resources (HR)",
    "IT Support Specialist": "Information Technology (IT)",
    "Compensation and Benefits Specialist": "Human Resources (HR)",
    "Web Developer": "Information Technology (IT)",
    "Customer Service Representative": "Customer Support",
    "Market Research Analyst": "Research and Development (R&D)",
    "Financial Analyst": "Finance and Accounting",
    "HR Generalist": "Human Resources (HR)",
    "Legal Assistant": "Legal and Compliance",
    "Cybersecurity Analyst": "Information Technology (IT)",
    "Project Manager": "Project Management",
    "Network Administrator": "Information Technology (IT)",
    "Team Lead": "Operations",
    "Research Analyst": "Research and Development (R&D)",
    "Help Desk Analyst": "Information Technology (IT)",
    "Innovation Manager": "Research and Development (R&D)",
    "Sales Representative": "Sales and Marketing",
    "Project Coordinator": "Project Management",
    "HR Manager": "Human Resources (HR)",
    "Operations Manager": "Operations",
    "CFO (Chief Financial Officer)": "Finance and Accounting",
    "CMO (Chief Marketing Officer)": "Sales and Marketing",
    "CTO (Chief Technology Officer)": "Information Technology (IT)",
    "CEO (Chief Executive Officer)": "Business Development",
}

departments_to_jobroles = {
    "Finance and Accounting": [
        "Accountant",
        "Financial Controller",
        "Auditor",
        "Tax Specialist",
        "Treasury Analyst",
        "Financial Analyst",
        "CFO (Chief Financial Officer)",
    ],
    "Sales and Marketing": [
        "Marketing Manager",
        "Account Manager",
        "Digital Marketer",
        "Brand Manager",
        "Public Relations Specialist",
        "Sales Representative",
        "CMO (Chief Marketing Officer)",
    ],
    "Legal and Compliance": [
        "Corporate Counsel",
        "Regulatory Affairs Specialist",
        "Compliance Officer",
        "Legal Assistant",
    ],
    "Research and Development (R&D)": [
        "Product Development Manager",
        "Research Scientist",
        "Market Research Analyst",
        "Research Analyst",
        "Innovation Manager",
    ],
    "Human Resources (HR)": [
        "Employee Relations Specialist",
        "Training and Development Manager",
        "Recruitment Specialist",
        "Compensation and Benefits Specialist",
        "HR Generalist",
        "HR Manager",
    ],
    "Operations": [
        "Production Supervisor",
        "Supply Chain Manager",
        "Warehouse Manager",
        "Logistics Coordinator",
        "Team Lead",
        "Operations Manager",
    ],
    "Customer Support": [
        "Call Center Supervisor",
        "Customer Support Specialist",
        "Customer Service Representative",
    ],
    "Information Technology (IT)": [
        "Database Administrator",
        "IT Manager",
        "Systems Analyst",
        "Software Engineer",
        "IT Support Specialist",
        "Web Developer",
        "Cybersecurity Analyst",
        "Network Administrator",
        "Help Desk Analyst",
        "CTO (Chief Technology Officer)",
    ],
    "Quality Assurance (QA)": ["Quality Control Analyst"],
    "Project Management": ["Scrum Master", "Project Manager", "Project Coordinator"],
    "Business Development": ["CEO (Chief Executive Officer)"],
}

skills_to_department = {
    "Research and Development (R&D)": {
        "Technical Skills": [
            "Research Methodology and Design",
            "Data Analysis and Interpretation",
            "Experimental Design and Prototyping",
            "Statistical Analysis and Modeling",
            "Programming and Software Development",
            "Technical Writing and Documentation",
            "Intellectual Property Management",
            "Project Management",
            "Laboratory Techniques and Equipment",
            "Quality Control and Assurance",
        ],
        "Non-Technical Skills": [
            "Critical Thinking and Problem Solving",
            "Creativity and Innovation",
            "Analytical Skills",
            "Communication and Presentation Skills",
            "Collaboration and Teamwork",
            "Time Management and Prioritization",
            "Adaptability and Flexibility",
            "Leadership and Mentoring",
            "Strategic Thinking",
            "Networking and Relationship Building",
        ],
    },
    "Project Management": {
        "Technical Skills": [
            "Project Planning and Scheduling",
            "Risk Management",
            "Budgeting and Financial Management",
            "Quality Management",
            "Stakeholder Management",
            "Resource Allocation and Management",
            "Contract and Procurement Management",
            "Project Monitoring and Control",
            "Change Management",
            "Reporting and Documentation",
        ],
        "Non-Technical Skills": [
            "Leadership and Team Management",
            "Communication and Negotiation Skills",
            "Problem Solving and Decision Making",
            "Time Management and Prioritization",
            "Conflict Resolution",
            "Strategic Thinking and Planning",
            "Adaptability and Flexibility",
            "Stakeholder Engagement",
            "Presentation and Public Speaking",
            "Continuous Improvement and Learning",
        ],
    },
    "Quality Assurance (QA)": {
        "Technical Skills": [
            "Quality Management Systems (QMS)",
            "Test Planning and Execution",
            "Test Automation",
            "Defect Tracking and Management",
            "Risk Assessment and Mitigation",
            "Statistical Process Control (SPC)",
            "Regulatory Compliance",
            "Root Cause Analysis",
            "Documentation and Standardization",
            "Validation and Verification",
        ],
        "Non-Technical Skills": [
            "Attention to Detail",
            "Analytical and Problem-Solving Skills",
            "Communication and Collaboration",
            "Time Management and Organization",
            "Critical Thinking",
            "Adaptability and Flexibility",
            "Process Improvement",
            "Teamwork and Interpersonal Skills",
            "Leadership and Mentoring",
            "Continuous Learning and Quality Mindset",
        ],
    },
    "Information Technology (IT)": {
        "Technical Skills": [
            "Programming and Software Development",
            "System Administration",
            "Network and Infrastructure Management",
            "Cybersecurity and Data Protection",
            "Database Management",
            "Cloud Computing",
            "IT Project Management",
            "IT Service Management",
            "IT Risk Assessment and Mitigation",
            "IT Troubleshooting and Support",
        ],
        "Non-Technical Skills": [
            "Problem Solving and Critical Thinking",
            "Communication and Collaboration",
            "Adaptability and Flexibility",
            "Time Management and Organization",
            "Customer Service and Relationship Management",
            "Leadership and Team Management",
            "Analytical and Data Interpretation Skills",
            "IT Governance and Compliance",
            "Continuous Learning and Professional Development",
            "Vendor Management and Contract Negotiation",
        ],
    },
    "Operations": {
        "Technical Skills": [
            "Supply Chain Management",
            "Process Optimization and Efficiency",
            "Inventory Management",
            "Logistics and Transportation",
            "Production Planning and Control",
            "Quality Control and Assurance",
            "Lean Six Sigma",
            "Data Analysis and Reporting",
            "Risk Management",
            "Cost Analysis and Budgeting",
        ],
        "Non-Technical Skills": [
            "Problem Solving and Decision Making",
            "Communication and Collaboration",
            "Leadership and Team Management",
            "Time Management and Prioritization",
            "Adaptability and Flexibility",
            "Analytical Thinking",
            "Negotiation and Conflict Resolution",
            "Continuous Improvement Mindset",
            "Strategic Thinking",
            "Customer Focus",
        ],
    },
    "Sales and Marketing": {
        "Technical Skills": [
            "Market Research and Analysis",
            "Customer Relationship Management (CRM)",
            "Digital Marketing and Analytics",
            "Sales Forecasting and Planning",
            "Advertising and Promotions",
            "Pricing Strategies and Competitive Analysis",
            "Social Media Marketing",
            "Product/Service Positioning and Branding",
            "Sales Funnel Management",
            "Sales Analytics and Reporting",
        ],
        "Non-Technical Skills": [
            "Communication and Interpersonal Skills",
            "Negotiation and Persuasion",
            "Relationship Building and Networking",
            "Strategic Thinking and Planning",
            "Creativity and Innovation",
            "Time Management and Prioritization",
            "Problem Solving and Decision Making",
            "Teamwork and Collaboration",
            "Adaptability and Flexibility",
            "Leadership and Mentoring",
        ],
    },
    "Customer Support": {
        "Technical Skills": [
            "Product Knowledge",
            "Troubleshooting and Problem Solving",
            "Ticketing Systems and CRM Software",
            "Communication Tools (e.g., Live Chat, Email)",
            "Remote Desktop and Screen Sharing",
            "Knowledge Base and Self-Service Platforms",
            "Customer Data Management",
            "Multi-Channel Support (Phone, Chat, Email)",
            "Technical Documentation and FAQ Creation",
            "Quality Assurance and Call Monitoring",
        ],
        "Non-Technical Skills": [
            "Communication and Active Listening",
            "Empathy and Customer Focus",
            "Problem Solving and Critical Thinking",
            "Patience and Resilience",
            "Time Management and Organization",
            "Conflict Resolution and Diplomacy",
            "Adaptability and Flexibility",
            "Teamwork and Collaboration",
            "Positive Attitude and Professionalism",
            "Continuous Learning and Skill Enhancement",
        ],
    },
    "Human Resources (HR)": {
        "Technical Skills": [
            "Recruitment and Selection",
            "Employee Onboarding and Offboarding",
            "Performance Management",
            "Compensation and Benefits Administration",
            "HRIS (Human Resources Information System) Management",
            "Employee Relations and Conflict Resolution",
            "HR Compliance and Legal Knowledge",
            "Training and Development",
            "HR Analytics and Reporting",
            "Employee Engagement and Retention",
        ],
        "Non-Technical Skills": [
            "Communication and Interpersonal Skills",
            "Confidentiality and Trustworthiness",
            "Problem Solving and Decision Making",
            "Empathy and Emotional Intelligence",
            "Time Management and Organization",
            "Leadership and Team Management",
            "Conflict Resolution and Mediation",
            "Adaptability and Flexibility",
            "Business Acumen and Strategic Thinking",
            "Ethical and Professional Conduct",
        ],
    },
    "Finance and Accounting": {
        "Technical Skills": [
            "Financial Analysis and Reporting",
            "Budgeting and Forecasting",
            "Financial Modeling",
            "Tax Planning and Compliance",
            "Auditing and Internal Controls",
            "Financial Statement Preparation",
            "Cost Accounting",
            "Cash Flow Management",
            "Risk Management and Analysis",
            "ERP (Enterprise Resource Planning) System Proficiency",
        ],
        "Non-Technical Skills": [
            "Analytical and Critical Thinking",
            "Attention to Detail",
            "Problem Solving and Decision Making",
            "Communication and Presentation Skills",
            "Time Management and Organization",
            "Ethical Conduct and Professionalism",
            "Adaptability and Flexibility",
            "Teamwork and Collaboration",
            "Business Acumen and Strategic Thinking",
            "Continuous Learning and Keeping up with Regulatory Changes",
        ],
    },
    "Legal and Compliance": {
        "Technical Skills": [
            "Legal Research and Analysis",
            "Contract Drafting and Review",
            "Regulatory Compliance",
            "Risk Assessment and Management",
            "Intellectual Property Rights",
            "Litigation and Dispute Resolution",
            "Data Privacy and Protection",
            "Corporate Governance",
            "Employment Law and Labor Regulations",
            "Mergers and Acquisitions",
        ],
        "Non-Technical Skills": [
            "Analytical and Critical Thinking",
            "Attention to Detail",
            "Problem Solving and Decision Making",
            "Communication and Negotiation Skills",
            "Ethical Conduct and Professionalism",
            "Time Management and Organization",
            "Adaptability and Flexibility",
            "Legal Writing and Documentation",
            "Teamwork and Collaboration",
            "Continuous Learning and Staying Updated with Legal Developments",
        ],
    },
    "Business Development": {
        "Technical Skills": [
            "Market Research and Analysis",
            "Lead Generation and Prospecting",
            "Sales Strategy and Planning",
            "Competitive Analysis",
            "Customer Relationship Management (CRM)",
            "Contract Negotiation and Deal Closing",
            "Proposal and Pitch Development",
            "Financial Analysis and ROI Assessment",
            "Data Analytics and Reporting",
            "Partnership and Alliance Building",
        ],
        "Non-Technical Skills": [
            "Communication and Presentation Skills",
            "Relationship Building and Networking",
            "Negotiation and Persuasion Skills",
            "Problem Solving and Decision Making",
            "Adaptability and Flexibility",
            "Time Management and Organization",
            "Leadership and Teamwork",
            "Resilience and Persistence",
            "Creative Thinking and Innovation",
        ],
    },
}

all_skills = [
    "Communication and Presentation Skills",
    "ERP (Enterprise Resource Planning) System Proficiency",
    "Time Management and Organization",
    "Problem Solving and Decision Making",
    "Analytical and Critical Thinking",
    "Risk Management and Analysis",
    "Tax Planning and Compliance",
    "Continuous Learning and Keeping up with Regulatory Changes",
    "Auditing and Internal Controls",
    "Cash Flow Management",
    "Budgeting and Forecasting",
    "Cost Accounting",
    "Financial Modeling",
    "Ethical Conduct and Professionalism",
    "Teamwork and Collaboration",
    "Financial Analysis and Reporting",
    "Attention to Detail",
    "Adaptability and Flexibility",
    "Communication and Interpersonal Skills",
    "Market Research and Analysis",
    "Relationship Building and Networking",
    "Sales Forecasting and Planning",
    "Negotiation and Persuasion",
    "Sales Analytics and Reporting",
    "Digital Marketing and Analytics",
    "Strategic Thinking and Planning",
    "Leadership and Mentoring",
    "Creativity and Innovation",
    "Customer Relationship Management (CRM)",
    "Pricing Strategies and Competitive Analysis",
    "Social Media Marketing",
    "Product/Service Positioning and Branding",
    "Sales Funnel Management",
    "Advertising and Promotions",
    "Mergers and Acquisitions",
    "Legal Writing and Documentation",
    "Legal Research and Analysis",
    "Litigation and Dispute Resolution",
    "Regulatory Compliance",
    "Data Privacy and Protection",
    "Contract Drafting and Review",
    "Risk Assessment and Management",
    "Communication and Negotiation Skills",
    "Continuous Learning and Staying Updated with Legal Developments",
    "Corporate Governance",
    "Time Management and Prioritization",
    "Quality Control and Assurance",
    "Programming and Software Development",
    "Strategic Thinking",
    "Collaboration and Teamwork",
    "Data Analysis and Interpretation",
    "Statistical Analysis and Modeling",
    "Experimental Design and Prototyping",
    "Project Management",
    "Analytical Skills",
    "Intellectual Property Management",
    "Technical Writing and Documentation",
    "Laboratory Techniques and Equipment",
    "Critical Thinking and Problem Solving",
    "Research Methodology and Design",
    "Networking and Relationship Building",
    "Conflict Resolution and Mediation",
    "Business Acumen and Strategic Thinking",
    "Training and Development",
    "Recruitment and Selection",
    "Employee Relations and Conflict Resolution",
    "Ethical and Professional Conduct",
    "Employee Engagement and Retention",
    "HR Compliance and Legal Knowledge",
    "Leadership and Team Management",
    "HR Analytics and Reporting",
    "Performance Management",
    "Empathy and Emotional Intelligence",
    "Employee Onboarding and Offboarding",
    "Compensation and Benefits Administration",
    "HRIS (Human Resources Information System) Management",
    "Process Optimization and Efficiency",
    "Supply Chain Management",
    "Data Analysis and Reporting",
    "Logistics and Transportation",
    "Customer Focus",
    "Risk Management",
    "Continuous Improvement Mindset",
    "Inventory Management",
    "Production Planning and Control",
    "Communication and Collaboration",
    "Lean Six Sigma",
    "Analytical Thinking",
    "Cost Analysis and Budgeting",
    "Financial Statement Preparation",
    "Continuous Learning and Skill Enhancement",
    "Ticketing Systems and CRM Software",
    "Product Knowledge",
    "Patience and Resilience",
    "Quality Assurance and Call Monitoring",
    "Positive Attitude and Professionalism",
    "Problem Solving and Critical Thinking",
    "Customer Data Management",
    "Knowledge Base and Self-Service Platforms",
    "Conflict Resolution and Diplomacy",
    "Communication and Active Listening",
    "Multi-Channel Support (Phone, Chat, Email)",
    "Troubleshooting and Problem Solving",
    "Communication Tools (e.g., Live Chat, Email)",
    "Employment Law and Labor Regulations",
    "Intellectual Property Rights",
    "Confidentiality and Trustworthiness",
    "IT Service Management",
    "IT Risk Assessment and Mitigation",
    "System Administration",
    "Customer Service and Relationship Management",
    "Database Management",
    "Vendor Management and Contract Negotiation",
    "Network and Infrastructure Management",
    "Cloud Computing",
    "Continuous Learning and Professional Development",
    "Cybersecurity and Data Protection",
    "Analytical and Data Interpretation Skills",
    "IT Troubleshooting and Support",
    "IT Project Management",
    "IT Governance and Compliance",
    "Root Cause Analysis",
    "Critical Thinking",
    "Test Planning and Execution",
    "Defect Tracking and Management",
    "Teamwork and Interpersonal Skills",
    "Test Automation",
    "Documentation and Standardization",
    "Risk Assessment and Mitigation",
    "Statistical Process Control (SPC)",
    "Continuous Learning and Quality Mindset",
    "Empathy and Customer Focus",
    "Remote Desktop and Screen Sharing",
    "Technical Documentation and FAQ Creation",
    "Negotiation and Conflict Resolution",
    "Project Monitoring and Control",
    "Resource Allocation and Management",
    "Stakeholder Engagement",
    "Budgeting and Financial Management",
    "Stakeholder Management",
    "Reporting and Documentation",
    "Continuous Improvement and Learning",
    "Conflict Resolution",
    "Change Management",
    "Presentation and Public Speaking",
    "Quality Management",
    "Project Planning and Scheduling",
    "Contract and Procurement Management",
    "Process Improvement",
    "Quality Management Systems (QMS)",
    "Validation and Verification",
    "Analytical and Problem-Solving Skills",
    "Partnership and Alliance Building",
    "Financial Analysis and ROI Assessment",
    "Creative Thinking and Innovation",
    "Negotiation and Persuasion Skills",
    "Leadership and Teamwork",
    "Lead Generation and Prospecting",
    "Competitive Analysis",
    "Resilience and Persistence",
    "Contract Negotiation and Deal Closing",
    "Sales Strategy and Planning",
    "Proposal and Pitch Development",
    "Data Analytics and Reporting",
]
