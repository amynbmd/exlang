/* tslint:disable:no-unused-variable */
import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { UserCardComponent } from './user-card.component';
import { User } from 'src/app/account/_models/user';
import { AccountTestingModule } from 'src/app/account/_testing/account-test.module';

describe('UserCardComponent', () => {
  let component: UserCardComponent;
  let fixture: ComponentFixture<UserCardComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      imports: [ UserCardComponent, AccountTestingModule ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    const user: User = {
      name: "name",
      email: "email@email.com",
      password: "P@ssWord",
      profile: {
        email: "email@email.com",
        wordofTheDay: "wordofTheDay",
        isOnline: true,
        countryCode: "countryCode",
        picURL: "picURL",
        bio: "bio",
        nativeLang: "nativeLang",
        learningLang: ["learningLang"],
        level: "level",
        interests: ["interests"],
        connected: false
      }

    };

    fixture = TestBed.createComponent(UserCardComponent);
    component = fixture.componentInstance;
    component.user = user;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
