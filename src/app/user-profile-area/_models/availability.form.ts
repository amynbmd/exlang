import { FormArray, FormControl, FormGroup } from "@angular/forms";

export class AvailabilityForm {
    email: FormControl<string | null>;
    sunday: FormGroup<TimeForm>;
    monday: FormGroup<TimeForm>;
    tuesday: FormGroup<TimeForm>;
    wednesday: FormGroup<TimeForm>;
    thursday: FormGroup<TimeForm>;
    friday: FormGroup<TimeForm>;
    saturday: FormGroup<TimeForm>;
}


export class TimeForm {
    isAvailable: FormControl<boolean>;
    startTime: FormControl<string | null>;
    endTime: FormControl<string | null>;
}