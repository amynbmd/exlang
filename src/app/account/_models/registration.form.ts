import { FormControl } from "@angular/forms";

export interface RegistrationForm {
    email: FormControl<string>;
    username: FormControl<string>;
    password: FormControl<string>;
    confirmPassword: FormControl<string>;
    clientUri: FormControl<string>;
}