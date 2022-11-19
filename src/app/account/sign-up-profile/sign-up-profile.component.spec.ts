/* tslint:disable:no-unused-variable */
import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { SignUpProfileComponent } from './sign-up-profile.component';
import { AccountTestingModule } from '../_testing/account-test.module';
import { TestingModule } from 'src/app/_modules/testing.module';

describe('SignUpProfileComponent', () => {
  let component: SignUpProfileComponent;
  let fixture: ComponentFixture<SignUpProfileComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      imports: [ SignUpProfileComponent, TestingModule],
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
