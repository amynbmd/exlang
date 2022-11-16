import { ChangeDetectionStrategy, ChangeDetectorRef, Component, OnInit } from '@angular/core';
import { MatSlideToggleModule } from '@angular/material/slide-toggle';
import { MatDividerModule } from '@angular/material/divider';
import { FormModule } from 'src/app/_modules/form.module';
import { MatButtonModule } from '@angular/material/button';
import { FormControl, FormGroup } from '@angular/forms';
import { AvailabilityForm, TimeForm } from '../../_models/availability.form';
import { Availability } from '../../_models/availability';
import { BaseComponent } from 'src/app/_shared/BaseComponent';
import { AuthenticationService } from 'src/app/account/_services/authentication/authentication.service';
import { RxwebValidators } from '@rxweb/reactive-form-validators';
import { User } from 'src/app/account/_models/user';

@Component({
  selector: 'app-availability',
  templateUrl: './availability.component.html',
  styleUrls: ['./availability.component.css'],
  changeDetection: ChangeDetectionStrategy.OnPush,
  standalone: true,

  imports: [
    MatSlideToggleModule,
    MatDividerModule,
    FormModule,
    MatButtonModule,
  ],
})
export class AvailabilityComponent extends BaseComponent implements OnInit {
  formGroup: FormGroup<AvailabilityForm>;

  user: User;
 

  constructor(private _authService: AuthenticationService, private _cd: ChangeDetectorRef) {
    super();
  }

  ngOnInit() {
    this.createForm();
    this.patchForm();
  }

  private createForm() {
    this.user = this._authService.getUserFromLocalStorage();

    this.formGroup = new FormGroup<AvailabilityForm>({
      email: new FormControl(this.user.email, {
        nonNullable: true,
        validators: [RxwebValidators.required(), RxwebValidators.email()],
      }),
      sunday: this.createTimeForm(),
      monday: this.createTimeForm(),
      tuesday: this.createTimeForm(),
      wednesday: this.createTimeForm(),
      thursday: this.createTimeForm(),
      friday: this.createTimeForm(),
      saturday: this.createTimeForm(),
    });
  }

  private patchForm() {
    this._authService.getUserAvailability(this.user.email).subscribe(response => {
      this.formGroup.patchValue(response);
    });
  }

  private createTimeForm() {
    let timeForm = new FormGroup<TimeForm>({
      isAvailable: new FormControl(false, {
        nonNullable: true,
        validators: [],
      }),
      startTime: new FormControl('', {
        nonNullable: true,
        validators: [],
      }),
      endTime: new FormControl('', {
        nonNullable: true,
        validators: [],
      }),
    });

    return timeForm;
  }

  submit() {
    this.summaryError = [];
    this.loading = true;
    const availability: Availability = this.formGroup.getRawValue();

    console.log(JSON.stringify(availability));

    this._authService.updateUserAvailability(availability).subscribe(response => {
      this._authService.setLoggedIn(response);
      console.log(response);

    },
    error => {
      this.summaryError.push(error.error.message);
      this._cd.markForCheck();
    }).
    add(() => {
      this.loading = false;  
    });
  }
}
