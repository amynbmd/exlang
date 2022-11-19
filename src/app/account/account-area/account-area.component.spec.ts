/* tslint:disable:no-unused-variable */
import { async, ComponentFixture, TestBed } from '@angular/core/testing';
import { By } from '@angular/platform-browser';
import { DebugElement } from '@angular/core';

import { AccountAreaComponent } from './account-area.component';
import { TestingModule } from 'src/app/_modules/testing.module';

describe('RegistrationAreaComponent', () => {
  let component: AccountAreaComponent;
  let fixture: ComponentFixture<AccountAreaComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      imports: [ AccountAreaComponent, TestingModule ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(AccountAreaComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
