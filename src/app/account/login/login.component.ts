import {
  ChangeDetectionStrategy,
  ChangeDetectorRef,
  Component,
  EventEmitter,
  OnInit,
  Output,
} from '@angular/core';
import { FormControl, FormGroup } from '@angular/forms';
import { MatCardModule } from '@angular/material/card';
import {MatCheckboxModule} from '@angular/material/checkbox';
import { MatProgressBarModule } from '@angular/material/progress-bar';
import { Router, RouterModule } from '@angular/router';
import { error, RxwebValidators } from '@rxweb/reactive-form-validators';
import { Login } from 'src/app/account/_models/login';
import { LoginForm } from 'src/app/account/_models/login.form';
import { FormModule } from 'src/app/_modules/form.module';
import { AuthenticationService } from 'src/app/account/_services/authentication/authentication.service';
import { BaseComponent } from '../../_shared/BaseComponent';
import { ShowComponent } from '../account-area/account-area.component';

@Component({
  selector: 'login',
  templateUrl: './login.component.html',
  styleUrls: ['./login.component.scss', '../_shared/styles.scss'],
  changeDetection: ChangeDetectionStrategy.OnPush,
  standalone: true,
  imports: [RouterModule, FormModule, MatCardModule, MatProgressBarModule, MatCheckboxModule],
})
export class LoginComponent extends BaseComponent implements OnInit {
  @Output() switchToForgotPasswordComponent = new EventEmitter<ShowComponent>();

  formGroup: FormGroup<LoginForm>;
  constructor(
    private _router: Router,
    private _authService: AuthenticationService,
    private _cd: ChangeDetectorRef,
  ) {
    super();
  }

  ngOnInit() {
    this.createForm();
  }

  private createForm() {
    this.formGroup = new FormGroup<LoginForm>({
      email: new FormControl('your@email.com', {
        nonNullable: true,
        validators: [RxwebValidators.required(), RxwebValidators.email()],
      }),
      password: new FormControl('123123123', {
        nonNullable: true,
        validators: [
          RxwebValidators.required(),
          // RxwebValidators.password({
          //   validation: { upperCase: true, lowerCase: true },
          // }),
          RxwebValidators.minLength({ value: 8 }),
        ],
      }),
      rememberMe: new FormControl(false, {
        nonNullable: true
      }),
    });
  }
  
  login() {
    this.loading = true;
    let credential: Login = this.formGroup.getRawValue();

    console.log(credential);

    this._authService.login(credential).subscribe(response => {
      console.log(response);

      this._router.navigate(['user-profile-area']);

    },
    error => {
      this.summaryError.push("Incorrect Email Address or Password. Please try again.");
      this._cd.markForCheck();
    })
  }

  switchToForgotPassword() {
    this.switchToForgotPasswordComponent.emit(ShowComponent.forgotPassword);
  }
}
