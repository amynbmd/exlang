export class BaseComponent {
    loading: boolean = false;
    summaryError: string[] = [];

    resetStateOnSuccess() {
        this.summaryError = [];
        this.loading = false;
    }

    resetStateOnFailure() {
        this.loading = false;
    }
}
