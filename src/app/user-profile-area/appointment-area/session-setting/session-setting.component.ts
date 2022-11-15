import { ChangeDetectionStrategy, Component, OnInit } from '@angular/core';

import { FormModule } from 'src/app/_modules/form.module';
import {MatSelectModule} from '@angular/material/select';
import {MatButtonModule} from '@angular/material/button';
import { Timezone } from '../../_models/Timezone';
import { AuthenticationService } from 'src/app/account/_services/authentication/authentication.service';
import { Observable } from 'rxjs';
import { SelectItem } from 'src/app/_models/select-item';
import { SessionSettingForm } from '../../_models/session-setting.form';
import { FormControl, FormGroup } from '@angular/forms';
import { RxwebFormDirective } from '@rxweb/reactive-form-validators/directives/rx-form.directive';
import { RxwebValidators } from '@rxweb/reactive-form-validators';
import { SessionSetting } from '../../_models/session-setting';
import { BaseComponent } from 'src/app/_shared/BaseComponent';

@Component({
  selector: 'app-session-setting',
  templateUrl: './session-setting.component.html',
  styleUrls: ['./session-setting.component.css'],
  changeDetection: ChangeDetectionStrategy.OnPush,
  standalone: true,

  imports: [
    FormModule, MatSelectModule, MatButtonModule,
  ]
})
export class SessionSettingComponent extends BaseComponent implements OnInit {
  formGroup: FormGroup<SessionSettingForm>;

  constructor(private _authService: AuthenticationService) {
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
    console.log(SessionSetting)
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
