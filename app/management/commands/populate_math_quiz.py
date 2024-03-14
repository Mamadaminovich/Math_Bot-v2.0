from django.core.management.base import BaseCommand
from app.models import Math_Quiz

class Command(BaseCommand):
    help = 'Populate the Math_Quiz model with math questions and answers'

    def handle(self, *args, **options):
        math_data = [
        ("10 + 5", "15"),
        ("20 - 8", "12"),
        ("6 * 4", "24"),
        ("15 / 3", "5"),
        ("18 + 7", "25"),
        ("30 - 12", "18"),
        ("9 * 3", "27"),
        ("24 / 4", "6"),
        ("14 + 9", "23"),
        ("40 - 17", "23"),
        ("5 * 6", "30"),
        ("36 / 6", "6"),
        ("22 + 8", "30"),
        ("50 - 21", "29"),
        ("7 * 4", "28"),
        ("42 / 7", "6"),
        ("12 + 15", "27"),
        ("60 - 28", "32"),
        ("8 * 7", "56"),
        ("48 / 6", "8"),
        ("25 + 9", "34"),
        ("70 - 33", "37"),
        ("6 * 8", "48"),
        ("56 / 7", "8"),
        ("30 + 12", "42"),
        ("80 - 38", "42"),
        ("9 * 5", "45"),
        ("45 / 9", "5"),
        ("18 + 20", "38"),
        ("90 - 49", "41"),
        ("10 * 6", "60"),
        ("54 / 6", "9"),
        ("35 + 15", "50"),
        ("100 - 52", "48"),
        ("7 * 7", "49"),
        ("63 / 9", "7"),
        ("16 + 24", "40"),
        ("120 - 58", "62"),
        ("8 * 9", "72"),
        ("81 / 9", "9"),
        ("40 + 18", "58"),
        ("140 - 63", "77"),
        ("11 * 7", "77"),
        ("88 / 8", "11"),
        ("20 + 25", "45"),
        ("170 - 78", "92"),
        ("12 * 8", "96"),
        ("96 / 8", "12"),
        ("50 + 22", "72"),
        ("200 - 88", "112"),
        ("13 * 6", "78"),
        ("104 / 8", "13"),
        ("28 + 32", "60"),
        ("240 - 98", "142"),
        ("14 * 9", "126"),
        ("126 / 9", "14"),
        ("60 + 30", "90"),
        ("300 - 108", "192"),
        ("15 * 8", "120"),
        ("150 / 10", "15"),
        ("32 + 28", "60"),
        ("320 - 128", "192"),
        ("16 * 7", "112"),
        ("112 / 8", "14"),
        ("70 + 35", "105"),
        ("400 - 138", "262"),
        ("17 * 9", "153"),
        ("153 / 9", "17"),
        ("80 + 40", "120"),
        ("500 - 158", "342"),
        ("18 * 6", "108"),
        ("216 / 8", "27"),
        ("90 + 45", "135"),
        ("600 - 178", "422"),
        ("19 * 8", "152"),
        ("152 / 8", "19"),
        ("100 + 50", "150"),
        ("700 - 198", "502"),
        ("20 * 10", "200"),
        ("200 / 10", "20"),
        ("40 + 50", "90"),
        ("800 - 228", "572"),
        ("21 * 9", "189"),
        ("189 / 9", "21"),
        ("110 + 45", "155"),
        ("900 - 258", "642"),
        ("22 * 8", "176"),
        ("176 / 8", "22"),
        ("120 + 60", "180"),
        ("1000 - 288", "712"),
        ("23 * 7", "161"),
        ("161 / 7", "23"),
        ("130 + 70", "200"),
        ("1100 - 298", "802"),
        ("24 * 9", "216"),
        ("216 / 9", "24"),
        ("140 + 80", "220"),
        ("1200 - 328", "872"),
        ("25 * 10", "250"),
        ("250 / 10", "25"),
        ]

        for question, answer in math_data:
            Math_Quiz.objects.create(question=question, answer=answer)

        self.stdout.write(self.style.SUCCESS('Math questions added successfully'))
        
        
# python manage.py populate_math_quiz