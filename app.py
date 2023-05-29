from flask import Flask, jsonify, request
from constants import skills_to_department
from constants import jobroles
from constants import posts
from constants import departments
from constants import all_skills
from constants import jobrole_to_department
from constants import departments_to_jobroles
import pandas as pd
import pickle

app = Flask(__name__)

model = pickle.load(open("SalaryPredictor.pkl", "rb"))


@app.route("/constants")
def constants():
    return jsonify(
        {
            "departments": departments,
            "jobroles": departments_to_jobroles,
            "posts": posts,
            "skills": skills_to_department,
        }
    )


@app.route("/predict", methods=["POST"])
def predict():
    if request.method == "POST":
        data = request.get_json()
        employee_data = {
            "job_role": data["job_role"],
            "attendance": data["attendance"],
            "department": data["department"],
            "Post": data["post"],
            "Equity(in %)": data["equity"],
            "Experience(in years)": data["experience"],
            "nClients": data["n_clients"],
            "test_scores(out of 100)": data["test_scores"],
            "skills": data["skills"],
        }
        if (
            employee_data["department"] not in departments
            or employee_data["Post"] not in posts
            or employee_data["job_role"] not in jobroles
        ):
            return jsonify(
                {
                    "success": False,
                    "msg": "Something in wrong with the Job role, Post or the Department",
                }
            )

        if (
            jobrole_to_department[employee_data["job_role"]]
            != employee_data["department"]
        ):
            return jsonify(
                {
                    "success": False,
                    "msg": "This job role is not present in this department",
                }
            )

        for skill in employee_data["skills"]:
            if (
                skill
                not in skills_to_department[employee_data["department"]][
                    "Technical Skills"
                ]
                and skill
                not in skills_to_department[employee_data["department"]][
                    "Non-Technical Skills"
                ]
            ):
                print(skill)
                return jsonify(
                    {
                        "success": False,
                        "msg": "The skill entered do not belong to the corresponding department",
                    }
                )

        if (
            employee_data["job_role"] == "CEO (Chief Executive Officer)"
            and employee_data["department"] == "Business Development"
        ):
            return jsonify({"success": True, "Predicted Salary": 797000})

        all_cols = [
            "job_role",
            "attendance",
            "department",
            "Post",
            "Equity(in %)",
            "Experience(in years)",
            "nClients",
            "test_scores(out of 100)",
        ]
        all_cols.extend(all_skills)

        emp_data = [[]]

        for i in all_cols:
            if i in employee_data:
                emp_data[0].append(employee_data[i])
            elif i not in employee_data and i not in employee_data["skills"]:
                emp_data[0].append(0)
            elif i in employee_data["skills"]:
                emp_data[0].append(1)

        prediction = model.predict(pd.DataFrame(emp_data, columns=all_cols))

        return jsonify({"success": True, "Predicted Salary": int(prediction[0])})


if __name__ == "__main__":
    app.run()
