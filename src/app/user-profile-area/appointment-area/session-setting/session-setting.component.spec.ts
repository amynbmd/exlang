/* tslint:disable:no-unused-variable */
import { async, ComponentFixture, TestBed } from '@angular/core/testing';
import { AccountTestingModule } from 'src/app/account/_testing/account-test.module';

import { SessionSettingComponent } from './session-setting.component';

describe('SessionSettingComponent', () => {
  let component: SessionSettingComponent;
  let fixture: ComponentFixture<SessionSettingComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      imports: [ SessionSettingComponent, AccountTestingModule ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(SessionSettingComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
