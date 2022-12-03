/* tslint:disable:no-unused-variable */
import { async, ComponentFixture, TestBed } from '@angular/core/testing';
import { By } from '@angular/platform-browser';
import { DebugElement } from '@angular/core';

import { ConnectionsComponent } from './connections.component';
import { AccountTestingModule } from '../account/_testing/account-test.module';

describe('ConnectionsComponent', () => {
  let component: ConnectionsComponent;
  let fixture: ComponentFixture<ConnectionsComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      imports: [ ConnectionsComponent, AccountTestingModule ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(ConnectionsComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
