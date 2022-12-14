import {
  ChangeDetectionStrategy,
  ChangeDetectorRef,
  Component,
  OnInit,
} from '@angular/core';
import { FormControl, FormGroup, ValidatorFn } from '@angular/forms';
import { MatCardModule } from '@angular/material/card';
import { MatProgressBarModule } from '@angular/material/progress-bar';
import { Router } from '@angular/router';
import { RxwebValidators } from '@rxweb/reactive-form-validators';
import { Registration } from 'src/app/account/_models/registration';
import { RegistrationForm } from 'src/app/account/_models/registration.form';
import { FormModule } from 'src/app/_modules/form.module';
import { AuthenticationService } from 'src/app/account/_services/authentication/authentication.service';
import { BaseComponent } from '../../_shared/BaseComponent';

@Component({
  selector: 'registration',
  templateUrl: './registration.component.html',
  styleUrls: ['./registration.component.scss', '../_shared/styles.scss'],
  changeDetection: ChangeDetectionStrategy.OnPush,
  standalone: true,
  imports: [
    FormModule,
    MatCardModule,
    MatProgressBarModule,
  ],
})
export class RegistrationComponent extends BaseComponent implements OnInit {
  formGroup: FormGroup<RegistrationForm>;
  constructor(
    private _router: Router,
    private _authService: AuthenticationService,
    private _cd: ChangeDetectorRef
  ) {
    super();
  }

  ngOnInit() {
    this.createForm();
  }

  
  private createForm() {
    this.formGroup = new FormGroup<RegistrationForm>({
      name: new FormControl('', {
        nonNullable: true,
        validators: [RxwebValidators.required()],
      }),
      email: new FormControl('', {
        nonNullable: true,
        validators: [RxwebValidators.required(), RxwebValidators.email()],
      }),
      password: new FormControl('', {
        nonNullable: true,
        validators: [...this.basePasswordValidatorFn()],
      }),
      confirmPassword: new FormControl('', {
        nonNullable: true,
        validators: [
          ...this.basePasswordValidatorFn(),
          RxwebValidators.compare({ fieldName: 'password' }),
        ],
      })
    });
  }

  private basePasswordValidatorFn() {
    let validators: ValidatorFn[] = [
      RxwebValidators.required(),
      // RxwebValidators.password({
      //   validation: { upperCase: true, lowerCase: true },
      // }),
      RxwebValidators.minLength({ value: 8 }),
    ];

    return validators;
  }


  register() {
    this.loading = true;

    //Prevent from clicking twice
    //this.formGroup.disable();
    const registration: Registration = this.formGroup.getRawValue();

    this.summaryError = [];

    this._authService.register(registration).subscribe(response => {
      this._authService.setLoggedIn(response);


      if (!this._authService.userHasProfile(response.profile)) {
        this._router.navigate(['account', 'area'], { queryParams: {completeProfile: false}})
        .then(() => {
          window.location.reload();
        });

      } else {
        this._router.navigate(['user-profile-area']);
      }

    },
    error => {
      this.summaryError.push(error.error.message);
      this._cd.markForCheck();
    }).
    add(() => {
      this.loading = false;  
    });

  }

  login() {
    this._router.navigate(['account', 'login']);
  }
}
