/* tslint:disable:no-unused-variable */
import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { SidebarComponent } from './sidebar.component';
import { HttpClientTestingModule } from '@angular/common/http/testing';
import { CookieModule } from 'ngx-cookie';
import { AuthenticationService } from 'src/app/account/_services/authentication/authentication.service';
import { JwtHelperService, JWT_OPTIONS } from '@auth0/angular-jwt';
import { MatMenuModule } from '@angular/material/menu';

describe('SidebarComponent', () => {
  let component: SidebarComponent;
  let fixture: ComponentFixture<SidebarComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [SidebarComponent],
      imports: [HttpClientTestingModule, CookieModule.withOptions(), MatMenuModule],
      providers: [AuthenticationService, JwtHelperService, { provide: JWT_OPTIONS, useValue: JWT_OPTIONS },],
    }).compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(SidebarComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
