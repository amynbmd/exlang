/* tslint:disable:no-unused-variable */
import { async, ComponentFixture, TestBed } from '@angular/core/testing';
import { AccountTestingModule } from '../account/_testing/account-test.module';

import { UserProfileAreaComponent } from './user-profile-area.component';

describe('UserProfileAreaComponent', () => {
  let component: UserProfileAreaComponent;
  let fixture: ComponentFixture<UserProfileAreaComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      imports: [ UserProfileAreaComponent, AccountTestingModule ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(UserProfileAreaComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
