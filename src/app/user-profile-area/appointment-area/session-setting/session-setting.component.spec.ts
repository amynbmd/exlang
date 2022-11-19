/* tslint:disable:no-unused-variable */
import { async, ComponentFixture, TestBed } from '@angular/core/testing';
import { TestingModule } from 'src/app/_modules/testing.module';

import { SessionSettingComponent } from './session-setting.component';

describe('SessionSettingComponent', () => {
  let component: SessionSettingComponent;
  let fixture: ComponentFixture<SessionSettingComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      imports: [ SessionSettingComponent, TestingModule ]
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
