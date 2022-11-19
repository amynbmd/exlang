import { ChangeDetectionStrategy, ChangeDetectorRef, Component, OnInit } from '@angular/core';

import { FormModule } from 'src/app/_modules/form.module';
import {MatSelectModule} from '@angular/material/select';
import {MatButtonModule} from '@angular/material/button';
import { AuthenticationService } from 'src/app/account/_services/authentication/authentication.service';
import { Observable } from 'rxjs';
import { SelectItem } from 'src/app/_models/select-item';
import { SessionSettingForm } from '../../_models/session-setting.form';
import { FormControl, FormGroup } from '@angular/forms';
import { RxwebValidators } from '@rxweb/reactive-form-validators';
import { SessionSetting } from '../../_models/session-setting';
import { BaseComponent } from 'src/app/_shared/BaseComponent';
import { CommonModule } from '@angular/common';
import { MatFormField } from '@angular/material/form-field';
import { MatInputModule } from '@angular/material/input';

@Component({
  selector: 'app-session-setting',
  templateUrl: './session-setting.component.html',
  styleUrls: ['./session-setting.component.css'],
  changeDetection: ChangeDetectionStrategy.OnPush,
  standalone: true,

  imports: [
    FormModule,
    MatSelectModule, MatButtonModule
  ]
})
export class SessionSettingComponent extends BaseComponent implements OnInit {
  formGroup: FormGroup<SessionSettingForm>;

  constructor(private _authService: AuthenticationService, private _cd: ChangeDetectorRef) {
    super();
   }

  timezones$: Observable<SelectItem[]>;

  ngOnInit() {
    this.createForm();
    this.timezones$ = this._authService.getTimezones();
  }

  submit(){
    let SessionSetting: SessionSetting = this.formGroup.getRawValue();
    this.summaryError = [];
    console.log(JSON.stringify(SessionSetting))

    this._authService.updateSessionSetting(SessionSetting).subscribe(response => {
    },
    error => {
      this.summaryError.push(error.error.message);
      this._cd.markForCheck();
    }).
    add(() => {
      this.loading = false;  
      this._cd.markForCheck();
    });
  }

  private createForm(){
    const user = this._authService.getUserFromLocalStorage();

    this.formGroup = new FormGroup<SessionSettingForm>({
      sessionDuration: new FormControl(null, {
        nonNullable: true,
        validators: [RxwebValidators.required()],
      }),       
      peopleBook: new FormControl('', {
        nonNullable: true,
        validators: [RxwebValidators.required()],
      }),  
      timeZone: new FormControl('', {
        nonNullable: true,
        validators: [RxwebValidators.required()],
      }),
      email: new FormControl(user.email, {
        nonNullable: true,
        validators: [RxwebValidators.email(), RxwebValidators.required()],
      }),
    });
  }

}
