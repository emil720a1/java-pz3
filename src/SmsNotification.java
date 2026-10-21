public final class SmsNotification extends Notification {
    private final String sender;

    public SmsNotification(String recipient, String sender) {
        super(recipient);
        this.sender = sender;
    }

    @Override
    public String formatMessage(String message) {
        return "SMS -> " + getRecipient() + " | Відправник: " + sender + " | " + message;
    }
}
