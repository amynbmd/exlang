/* tslint:disable:no-unused-variable */
import { async, ComponentFixture, TestBed } from '@angular/core/testing';
import { By } from '@angular/platform-browser';
import { DebugElement } from '@angular/core';

import { CommunityConnectionsComponent } from './community-connections.component';
import { AccountTestingModule } from '../account/_testing/account-test.module';

describe('CommunityConnectionsComponent', () => {
  let component: CommunityConnectionsComponent;
  let fixture: ComponentFixture<CommunityConnectionsComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      imports: [ CommunityConnectionsComponent, AccountTestingModule ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(CommunityConnectionsComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
