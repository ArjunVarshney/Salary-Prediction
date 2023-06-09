# Salary Prediction Model

This is a salary prediction model which takes in the equity percentage, post, department, skills, jobrole, experience, test_scores, number of clients of a specific employee to predict the salary of that employee.

**Model used**: "Linear Regression"
**Library**: "Scikit-learn"

## How to run:

- Install the necessary packages using `pip install ....`
- Run the `app.py` file using `python app.py`
- The app will start running at `localhost:5000`
- Hit the endpoints for the desire output (the details of the endpoints are given below)

## End points for api:

### **/predict** (Post):

> "complete url": http://127.0.0.1:5000/predict

This endpoint return the prediction of the model based on the give input.

sample request body :-

```json
{
  "job_role": "IT Manager",
  "attendance": 93,
  "department": "Information Technology (IT)",
  "post": "Mid-Level/Intermediate",
  "equity": 1.6,
  "experience": 8,
  "n_clients": 90,
  "test_scores": 87,
  "skills": [
    "Database Management",
    "Cloud Computing",
    "IT Project Management",
    "IT Service Management",
    "Time Management and Organization",
    "Customer Service and Relationship Management",
    "Leadership and Team Management",
    "Analytical and Data Interpretation Skills"
  ]
}
```

sample response :-

```json
{
  "Predicted Salary": 130924,
  "success": true
}
```

## **/constants** (Get):

> "complete url": http://127.0.0.1:5000/constants

This end point return the constants that the model will work for otherwise it won't work.

sample response :-

```json
{
  "departments": [
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
    "Business Development"
  ],
  "jobroles": {
    "Business Development": ["CEO (Chief Executive Officer)"],
    "Customer Support": [
      "Call Center Supervisor",
      "Customer Support Specialist",
      "Customer Service Representative"
    ],
    "Finance and Accounting": [
      "Accountant",
      "Financial Controller",
      "Auditor",
      "Tax Specialist",
      "Treasury Analyst",
      "Financial Analyst",
      "CFO (Chief Financial Officer)"
    ],
    "Human Resources (HR)": [
      "Employee Relations Specialist",
      "Training and Development Manager",
      "Recruitment Specialist",
      "Compensation and Benefits Specialist",
      "HR Generalist",
      "HR Manager"
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
      "CTO (Chief Technology Officer)"
    ],
    "Legal and Compliance": [
      "Corporate Counsel",
      "Regulatory Affairs Specialist",
      "Compliance Officer",
      "Legal Assistant"
    ],
    "Operations": [
      "Production Supervisor",
      "Supply Chain Manager",
      "Warehouse Manager",
      "Logistics Coordinator",
      "Team Lead",
      "Operations Manager"
    ],
    "Project Management": [
      "Scrum Master",
      "Project Manager",
      "Project Coordinator"
    ],
    "Quality Assurance (QA)": ["Quality Control Analyst"],
    "Research and Development (R&D)": [
      "Product Development Manager",
      "Research Scientist",
      "Market Research Analyst",
      "Research Analyst",
      "Innovation Manager"
    ],
    "Sales and Marketing": [
      "Marketing Manager",
      "Account Manager",
      "Digital Marketer",
      "Brand Manager",
      "Public Relations Specialist",
      "Sales Representative",
      "CMO (Chief Marketing Officer)"
    ]
  },
  "posts": [
    "Entry Level/Junior",
    "Associate/Specialist",
    "Mid-Level/Intermediate",
    "Senior/Lead",
    "Manager/Supervisor",
    "Director/Head",
    "Vice President/Executive"
  ],
  "skills": {
    "Business Development": {
      "Non-Technical Skills": [
        "Communication and Presentation Skills",
        "Relationship Building and Networking",
        "Negotiation and Persuasion Skills",
        "Problem Solving and Decision Making",
        "Adaptability and Flexibility",
        "Time Management and Organization",
        "Leadership and Teamwork",
        "Resilience and Persistence",
        "Creative Thinking and Innovation"
      ],
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
        "Partnership and Alliance Building"
      ]
    },
    "Customer Support": {
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
        "Continuous Learning and Skill Enhancement"
      ],
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
        "Quality Assurance and Call Monitoring"
      ]
    },
    "Finance and Accounting": {
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
        "Continuous Learning and Keeping up with Regulatory Changes"
      ],
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
        "ERP (Enterprise Resource Planning) System Proficiency"
      ]
    },
    "Human Resources (HR)": {
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
        "Ethical and Professional Conduct"
      ],
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
        "Employee Engagement and Retention"
      ]
    },
    "Information Technology (IT)": {
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
        "Vendor Management and Contract Negotiation"
      ],
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
        "IT Troubleshooting and Support"
      ]
    },
    "Legal and Compliance": {
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
        "Continuous Learning and Staying Updated with Legal Developments"
      ],
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
        "Mergers and Acquisitions"
      ]
    },
    "Operations": {
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
        "Customer Focus"
      ],
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
        "Cost Analysis and Budgeting"
      ]
    },
    "Project Management": {
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
        "Continuous Improvement and Learning"
      ],
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
        "Reporting and Documentation"
      ]
    },
    "Quality Assurance (QA)": {
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
        "Continuous Learning and Quality Mindset"
      ],
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
        "Validation and Verification"
      ]
    },
    "Research and Development (R&D)": {
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
        "Networking and Relationship Building"
      ],
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
        "Quality Control and Assurance"
      ]
    },
    "Sales and Marketing": {
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
        "Leadership and Mentoring"
      ],
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
        "Sales Analytics and Reporting"
      ]
    }
  }
}
```
