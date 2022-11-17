import { CommonModule } from '@angular/common';
import { ChangeDetectionStrategy, Component, OnInit } from '@angular/core';
import { MatCardModule } from '@angular/material/card';
import { ActivatedRoute, ActivationStart, Router } from '@angular/router';
import { ForgotPasswordComponent } from '../forgot-password/forgot-password.component';
import { LoginComponent } from '../login/login.component';
import { RegistrationComponent } from '../registration/registration.component';
import { SignUpProfileComponent } from '../sign-up-profile/sign-up-profile.component';

@Component({
  selector: 'app-account-area',
  templateUrl: './account-area.component.html',
  styleUrls: ['./account-area.component.scss'],
  changeDetection: ChangeDetectionStrategy.OnPush,
  standalone: true,
  imports: [
    CommonModule,
    MatCardModule,
    RegistrationComponent,
    LoginComponent,
    ForgotPasswordComponent,
    SignUpProfileComponent
  ],
})
export class AccountAreaComponent implements OnInit {
  showComponent: ShowComponent = ShowComponent.login;

  constructor(private _route: ActivatedRoute, private _router: Router) { }

  ngOnInit() {
    if (this._route.snapshot.queryParamMap.get('completeProfile')?.trim().toLowerCase() == 'false') {
      this.showComponent = ShowComponent.completeProfile;
    }
  }

  switchToRegister() {
    this.showComponent = ShowComponent.register;
  }

  switchToLogin() {
    this.showComponent = ShowComponent.login;
  }

  switchToForgotPassword(value: ShowComponent) {
    this.showComponent = value;
  }
}

export enum ShowComponent {
  register = 0, 
  login = 1,
  forgotPassword = 2,
  completeProfile = 3
}