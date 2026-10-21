public final class PushNotification extends Notification {
    private final String application;

    public PushNotification(String recipient, String application) {
        super(recipient);
        this.application = application;
    }

    @Override
    public String formatMessage(String message) {
        return "PUSH -> " + getRecipient() + " | Застосунок: " + application + " | " + message;
    }
}
