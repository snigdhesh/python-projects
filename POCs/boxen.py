from services import utils
from boxen import boxen

salary1 = utils.calculate_salary(10,50)
print(f"+{salary1} credited to your account!")

styles = {
    "padding": 3,
    "borderStyle": "double",
    "borderColor": "red",
    "dimBorder": False,
    "textAlignment": "left",
    "float": "left",
}



print(
    boxen(f"+{salary1} credited to your account!", options=styles)
)