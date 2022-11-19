/* tslint:disable:no-unused-variable */
import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { UserBioComponent } from './user-bio.component';
import { AccountTestingModule } from 'src/app/account/_testing/account-test.module';

describe('UserBioComponent', () => {
  let component: UserBioComponent;
  let fixture: ComponentFixture<UserBioComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      imports: [
        UserBioComponent,
        AccountTestingModule
      ],
    }).compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(UserBioComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
