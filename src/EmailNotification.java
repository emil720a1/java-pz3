public final class EmailNotification extends Notification {
    private final String subject;

    public EmailNotification(String recipient, String subject) {
        super(recipient);
        this.subject = subject;
    }

    @Override
    public String formatMessage(String message) {
        return "EMAIL -> " + getRecipient() + " | Тема: " + subject + " | " + message;
    }
}
