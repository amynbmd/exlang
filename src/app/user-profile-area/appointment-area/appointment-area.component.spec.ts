/* tslint:disable:no-unused-variable */
import { async, ComponentFixture, TestBed } from '@angular/core/testing';
import { By } from '@angular/platform-browser';
import { DebugElement } from '@angular/core';

import { AppointmentAreaComponent } from './appointment-area.component';
import { TestingModule } from 'src/app/_modules/testing.module';

describe('AppointmentAreaComponent', () => {
  let component: AppointmentAreaComponent;
  let fixture: ComponentFixture<AppointmentAreaComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      imports: [ AppointmentAreaComponent ]
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
