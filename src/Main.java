public class Main {
    public static void main(String[] args) {
        Notification[] notifications = {
            new EmailNotification("oleh.bondarenko@example.com", "Лабораторна робота №3"),
            new SmsNotification("+380671234567", "DUІKT"),
            new PushNotification("bondarenko_oleh", "Student App")
        };

        String message = "Роботу успішно підготовлено до захисту.";
        for (Notification notification : notifications) {
            System.out.println(notification.formatMessage(message));
        }

        // Для додавання нового різновиду достатньо створити клас-нащадок.
        // Цикл вище змінювати не потрібно.
    }
}
