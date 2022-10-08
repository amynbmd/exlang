import { CommonModule } from '@angular/common';
import { ChangeDetectionStrategy, Component, OnInit } from '@angular/core';
import { MatCardModule } from '@angular/material/card';
import { LoginComponent } from '../login/login.component';
import { RegistrationComponent } from '../registration/registration.component';

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
    LoginComponent
  ],
})
export class AccountAreaComponent implements OnInit {
  showComponent: ShowComponent = ShowComponent.login;

  constructor() { }

  ngOnInit() {
  }

  switchToRegister() {
    this.showComponent = ShowComponent.register;
  }

  switchToLogin() {
    this.showComponent = ShowComponent.login;
  }
}

export enum ShowComponent {
  register = 0, 
  login = 1
}