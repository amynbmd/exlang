import { FormControl } from "@angular/forms";

export class SignUpProfileForm {
    email: FormControl<string | null>;
    countryCode: FormControl<string>;
    nativeLang: FormControl<string>;
    learningLangs: FormControl<string[]>;
    level: FormControl<string>;
    interest: FormControl<string>;
    bio: FormControl<string | null>;
}
