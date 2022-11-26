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
import { getMatIconFailedToSanitizeLiteralError } from '@angular/material/icon';
import { Profile } from '../_models/profile';

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
      email: new FormControl('duyen@email.com', {
        nonNullable: true,
        validators: [RxwebValidators.required(), RxwebValidators.email()],
      }),
      password: new FormControl('321654987', {
        nonNullable: true,
        validators: [
          RxwebValidators.required(),
          // RxwebValidators.password({
          //   validation: { upperCase: true, lowerCase: true },
          // }),
          RxwebValidators.minLength({ value: 8 }),
        ],
      })
    });
  }
  
  login() {
    this.loading = true;
    let credential: Login = this.formGroup.getRawValue();

    this.summaryError = [];

    this._authService.login(credential).subscribe(response => {
      this._authService.setLoggedIn(response);

      if (!this._authService.userHasProfile(response.profile)) {
        this._router.navigate(['account', 'area'], { queryParams: {completeProfile: false}})
        .then(() => {
          window.location.reload();
        });;

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
      this._cd.markForCheck();
    });
  }

  switchToForgotPassword() {
    this.switchToForgotPasswordComponent.emit(ShowComponent.forgotPassword);
  }

}
/*
export class Profile {
    email: string;
    wordofTheDay: string;
    : boolean;
    : string;
    : string;
    : string;
    : string;
    : string[];
    : string;
    interests: string[];
}
*/