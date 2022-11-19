/* tslint:disable:no-unused-variable */
import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { UserProfileAreaComponent } from './user-profile-area.component';
import { TestingModule } from '../_modules/testing.module';

describe('UserProfileAreaComponent', () => {
  let component: UserProfileAreaComponent;
  let fixture: ComponentFixture<UserProfileAreaComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      imports: [ UserProfileAreaComponent ]
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
