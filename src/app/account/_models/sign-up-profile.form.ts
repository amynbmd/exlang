import { FormControl } from "@angular/forms";

export class SignUpProfileForm {
    countryCode: FormControl<string>;
    nativeLang: FormControl<string>;
    learningLangs: FormControl<string[]>;
    level: FormControl<string>;
    interest: FormControl<string>;
}
