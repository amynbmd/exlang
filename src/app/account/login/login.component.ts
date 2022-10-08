import {
  ChangeDetectionStrategy,
  ChangeDetectorRef,
  Component,
  OnInit,
} from '@angular/core';
import { FormControl, FormGroup } from '@angular/forms';
import { MatCardModule } from '@angular/material/card';
import { MatProgressBarModule } from '@angular/material/progress-bar';
import { Router, RouterModule } from '@angular/router';
import { RxwebValidators } from '@rxweb/reactive-form-validators';
import { Login } from 'src/app/account/_models/login';
import { LoginForm } from 'src/app/account/_models/login.form';
import { FormModule } from 'src/app/_modules/form.module';
import { AuthenticationService } from 'src/app/account/_services/authentication/authentication.service';
import { BaseComponent } from '../../_shared/BaseComponent';

@Component({
  selector: 'account-login',
  templateUrl: './login.component.html',
  styleUrls: ['./login.component.scss', '../_shared/styles.scss'],
  changeDetection: ChangeDetectionStrategy.OnPush,
  standalone: true,
  imports: [RouterModule, FormModule, MatCardModule, MatProgressBarModule],
})
export class LoginComponent extends BaseComponent implements OnInit {
  formGroup: FormGroup<LoginForm>;
  showResetPasswordBtn: boolean = false;

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
      email: new FormControl('', {
        nonNullable: true,
        validators: [RxwebValidators.required()],
      }),
      password: new FormControl('', {
        nonNullable: true,
        validators: [
          RxwebValidators.required(),
          RxwebValidators.password({
            validation: { upperCase: true, lowerCase: true },
          }),
          RxwebValidators.minLength({ value: 8 }),
        ],
      }),
    });
  }
  
  private checkWrongPassword() {
    if (this.formGroup.get('password')?.invalid) {
      if (
        this.formGroup.controls.password.errors?.['other']
          .toLowerCase()
          .indexOf('wrong password') != -1
      ) {
        this.showResetPasswordBtn = true;
      }
    }
  }

  login() {
    this.loading = true;
    let credential: Login = this.formGroup.getRawValue();
  }

  resetPassword() {
    this._router.navigate(['account', 'password', 'reset']);
  }

  registerAccount() {
    this._router.navigate(['account', 'register']);
  }
}
