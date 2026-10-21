public abstract class Notification {
    private final String recipient;

    protected Notification(String recipient) {
        if (recipient == null || recipient.isBlank()) {
            throw new IllegalArgumentException("Одержувач не може бути порожнім");
        }
        this.recipient = recipient;
    }

    public final String getRecipient() {
        return recipient;
    }

    public abstract String formatMessage(String message);
}
