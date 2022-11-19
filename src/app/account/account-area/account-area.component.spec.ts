/* tslint:disable:no-unused-variable */
import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { AccountAreaComponent } from './account-area.component';
import { AccountTestingModule } from '../_testing/account-test.module';

describe('RegistrationAreaComponent', () => {
  let component: AccountAreaComponent;
  let fixture: ComponentFixture<AccountAreaComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      imports: [ AccountAreaComponent, AccountTestingModule ]
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
