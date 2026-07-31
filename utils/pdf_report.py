from reportlab.platypus import SimpleDocTemplate, Paragraph
from reportlab.lib.styles import getSampleStyleSheet
from datetime import datetime


def generate_pdf(patient_data, prediction, probability):

    file_name = "Medical_Report.pdf"

    pdf = SimpleDocTemplate(file_name)

    styles = getSampleStyleSheet()

    elements = []

    elements.append(
        Paragraph("<b>Heart Disease AI Report</b>", styles["Title"])
    )

    elements.append(
        Paragraph(
            f"Generated: {datetime.now().strftime('%Y-%m-%d %H:%M')}",
            styles["Normal"]
        )
    )

    elements.append(
        Paragraph("<br/>", styles["Normal"])
    )

    elements.append(
        Paragraph("<b>Patient Information</b>", styles["Heading2"])
    )

    for key, value in patient_data.items():

        elements.append(
            Paragraph(f"{key}: {value}", styles["Normal"])
        )

    elements.append(
        Paragraph("<br/>", styles["Normal"])
    )

    elements.append(
        Paragraph("<b>Prediction</b>", styles["Heading2"])
    )

    elements.append(
        Paragraph(f"Result: {prediction}", styles["Normal"])
    )

    elements.append(
        Paragraph(
            f"Probability: {probability:.2f}%",
            styles["Normal"]
        )
    )

    elements.append(
        Paragraph("<br/>", styles["Normal"])
    )

    elements.append(
        Paragraph("<b>Recommendations</b>", styles["Heading2"])
    )

    if prediction == "High Risk":

        recommendations = [
            "Visit a cardiologist.",
            "Reduce smoking.",
            "Exercise regularly.",
            "Follow a healthy diet."
        ]

    else:

        recommendations = [
            "Maintain your healthy lifestyle.",
            "Exercise regularly.",
            "Monitor your health periodically."
        ]

    for rec in recommendations:

        elements.append(
            Paragraph(f"• {rec}", styles["Normal"])
        )

    pdf.build(elements)

    return file_name