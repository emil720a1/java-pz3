from reportlab.lib.enums import TA_CENTER, TA_JUSTIFY
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import mm
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, PageBreak, Preformatted

OUT = "/Users/mcaleg2006/Documents/Codex/2026-10-21/no-3-3-lsp-java-4/outputs/report_lab3_bondarenko_oleh.pdf"
FONT = "/System/Library/Fonts/Supplemental/Verdana.ttf"
FONT_BOLD = "/System/Library/Fonts/Supplemental/Verdana Bold.ttf"
pdfmetrics.registerFont(TTFont("Verdana", FONT))
pdfmetrics.registerFont(TTFont("Verdana-Bold", FONT_BOLD))

styles = getSampleStyleSheet()
styles.add(ParagraphStyle(name="UA", fontName="Verdana", fontSize=10, leading=15, alignment=TA_JUSTIFY, spaceAfter=7))
styles.add(ParagraphStyle(name="TitleUA", parent=styles["UA"], fontName="Verdana-Bold", fontSize=16, leading=21, alignment=TA_CENTER, spaceAfter=14))
styles.add(ParagraphStyle(name="HeadUA", parent=styles["UA"], fontName="Verdana-Bold", fontSize=12, leading=16, spaceBefore=8, spaceAfter=8))
styles.add(ParagraphStyle(name="SmallUA", parent=styles["UA"], fontSize=8.5, leading=12))
styles.add(ParagraphStyle(name="CodeUA", fontName="Verdana", fontSize=8, leading=11, leftIndent=8, rightIndent=8, backColor="#f2f4f7", borderPadding=6, spaceAfter=8))

def p(text, style="UA"):
    return Paragraph(text, styles[style])

def footer(canvas, doc):
    canvas.saveState()
    canvas.setFont("Verdana", 8)
    canvas.setFillColorRGB(0.35, 0.35, 0.35)
    canvas.drawString(20*mm, 12*mm, "Лабораторна робота №3 • Бондаренко Олег")
    canvas.drawRightString(190*mm, 12*mm, f"Сторінка {doc.page}")
    canvas.restoreState()

story = []
story += [p("ДЕРЖАВНИЙ УНІВЕРСИТЕТ ІНФОРМАЦІЙНО-КОМУНІКАЦІЙНИХ ТЕХНОЛОГІЙ", "TitleUA"),
          p("Кафедра технологій цифрового розвитку", "UA"), Spacer(1, 30),
          p("ЛАБОРАТОРНА РОБОТА №3", "TitleUA"),
          p("Тема: Успадкування, поліморфізм, принцип LSP<br/>Проєктування ієрархії з поліморфною обробкою", "UA"), Spacer(1, 25),
          p("Дисципліна: Конструювання програмного забезпечення Java", "UA"),
          p("Виконав: студент групи ТЦР-31<br/>Бондаренко Олег", "UA"), Spacer(1, 55),
          p("Київ — 2026", "UA"), PageBreak()]

story += [p("1. Мета та варіант роботи", "HeadUA"),
          p("Мета роботи — сформувати навички проєктування ієрархії класів із поліморфною обробкою через базовий тип та застосувати принцип підстановки Лісков (LSP). Обрано варіант 4: базовий тип «Сповіщення», різновиди Email, SMS, Push, спільна операція — формування тексту."),
          p("2. Структура ієрархії", "HeadUA"),
          p("Абстрактний клас Notification містить спільні дані recipient, перевірку одержувача та метод getRecipient(). Метод formatMessage(String message) оголошений абстрактним, оскільки спосіб формування повідомлення залежить від каналу."),
          p("Кожен різновид має власне специфічне поле: subject, sender або application — і перевизначає formatMessage. Конструктор кожного нащадка викликає super(recipient), тому спільна частина об’єкта ініціалізується централізовано без дублювання перевірок."),
          p("3. Ключові фрагменти реалізації", "HeadUA"),
          Preformatted("public abstract class Notification {\n    private final String recipient;\n\n    protected Notification(String recipient) {\n        if (recipient == null || recipient.isBlank())\n            throw new IllegalArgumentException();\n        this.recipient = recipient;\n    }\n\n    public abstract String formatMessage(String message);\n}", styles["CodeUA"]),
          Preformatted("Notification[] notifications = {\n    new EmailNotification(...),\n    new SmsNotification(...),\n    new PushNotification(...)\n};\n\nfor (Notification notification : notifications) {\n    System.out.println(notification.formatMessage(message));\n}", styles["CodeUA"]), PageBreak()]

story += [p("4. Поліморфна обробка", "HeadUA"),
          p("Масив і цикл працюють лише з базовим типом Notification. Перевірки instanceof та розгалуження за конкретними типами відсутні. Виклик formatMessage динамічно обирає реалізацію відповідного класу-нащадка."),
          p("Якщо додати, наприклад, TelegramNotification extends Notification, код циклу змінювати не потрібно. Достатньо реалізувати конструктор, викликати super(recipient) і перевизначити formatMessage."),
          p("5. Обґрунтування принципу LSP", "HeadUA"),
          p("Кожен нащадок можна передати туди, де очікується Notification, оскільки він має всі операції базового типу. Жоден нащадок не послаблює доступні можливості, не змінює контракт конструктора базової частини та не викидає несподіваних винятків для коректного повідомлення. Метод повертає рядок сформованого тексту для будь-якого підтримуваного каналу, тому очікувана поведінка клієнта зберігається."),
          p("6. Відповіді на контрольні питання", "HeadUA"),
          p("1. Обробка через базовий тип прибирає залежність клієнта від конкретних класів і дозволяє додавати нові різновиди без переписування алгоритму.<br/><br/>2. Спільний контракт оголошують у базовому типі, а відмінності реалізують через перевизначення методів у нащадках. Клієнт працює з базовим типом.<br/><br/>3. LSP означає, що об’єкт нащадка можна використовувати замість об’єкта базового типу без порушення очікуваного результату. Це перевіряють тестуванням клієнтського коду на всіх різновидах через посилання базового типу.<br/><br/>4. У базовий клас виносять спільні поля, інваріанти, перевірки та поведінку. Специфічні дані й алгоритми залишають у похідних класах."),
          p("7. Висновок", "HeadUA"),
          p("Створено ієрархію сповіщень із трьома різновидами. Поліморфний масив демонструє єдиний спосіб обробки, а використання super забезпечує коректну ініціалізацію базової частини. Архітектура відповідає принципу LSP і допускає розширення без зміни коду клієнта."),
          p("8. Посилання на репозиторій", "HeadUA"),
          p("https://github.com/emil720a1/java-pz3")]

doc = SimpleDocTemplate(OUT, pagesize=A4, rightMargin=20*mm, leftMargin=20*mm, topMargin=18*mm, bottomMargin=20*mm, title="Лабораторна робота №3 — Бондаренко Олег")
doc.build(story, onFirstPage=footer, onLaterPages=footer)
