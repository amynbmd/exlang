import { FormControl, FormGroup } from "@angular/forms";

export class SessionSettingForm {
    sessionDuration: FormControl<number | null>;
    peopleBook: FormControl<string>;
    timeZone: FormControl<string>;
    email: FormControl<string | null>;


    


}
