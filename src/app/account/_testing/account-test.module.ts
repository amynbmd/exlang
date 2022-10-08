import { HttpClientTestingModule } from '@angular/common/http/testing';
import { NgModule } from '@angular/core';
import { MatMenuModule } from '@angular/material/menu';
import { NoopAnimationsModule } from '@angular/platform-browser/animations';
import { RouterTestingModule } from '@angular/router/testing';
import { JwtHelperService, JWT_OPTIONS } from '@auth0/angular-jwt';
import { CookieModule } from 'ngx-cookie';
import { AuthenticationService } from '../_services/authentication/authentication.service';

@NgModule({
  imports: [
    NoopAnimationsModule,
    RouterTestingModule,
    HttpClientTestingModule,
    CookieModule.withOptions(),
    MatMenuModule,
  ],
  exports: [NoopAnimationsModule, RouterTestingModule, HttpClientTestingModule, MatMenuModule],
  providers: [
    AuthenticationService,
    JwtHelperService,
    { provide: JWT_OPTIONS, useValue: JWT_OPTIONS },
  ],
})
export class AccountTestingModule {}
