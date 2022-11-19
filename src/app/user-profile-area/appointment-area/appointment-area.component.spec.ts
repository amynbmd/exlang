/* tslint:disable:no-unused-variable */
import { async, ComponentFixture, TestBed } from '@angular/core/testing';
import { AccountTestingModule } from 'src/app/account/_testing/account-test.module';

import { AppointmentAreaComponent } from './appointment-area.component';

describe('AppointmentAreaComponent', () => {
  let component: AppointmentAreaComponent;
  let fixture: ComponentFixture<AppointmentAreaComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      imports: [ AppointmentAreaComponent, AccountTestingModule ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(AppointmentAreaComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
