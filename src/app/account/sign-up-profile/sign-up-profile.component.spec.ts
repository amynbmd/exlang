/* tslint:disable:no-unused-variable */
import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { SignUpProfileComponent } from './sign-up-profile.component';
import { AccountTestingModule } from '../_testing/account-test.module';

describe('SignUpProfileComponent', () => {
  let component: SignUpProfileComponent;
  let fixture: ComponentFixture<SignUpProfileComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      imports: [ SignUpProfileComponent, AccountTestingModule ],
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(SignUpProfileComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
