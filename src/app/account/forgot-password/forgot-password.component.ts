import { ChangeDetectionStrategy, Component, OnInit } from '@angular/core';
import { FormControl, FormGroup } from '@angular/forms';
import { password, RxwebValidators } from '@rxweb/reactive-form-validators';
import { FormModule } from 'src/app/_modules/form.module';
import { ForgotPassword } from '../_models/forgot-password';
import { ForgotPasswordForm } from '../_models/forgot-password.form';

@Component({
  selector: 'app-forgot-password',
  templateUrl: './forgot-password.component.html',
  styleUrls: ['./forgot-password.component.scss','../_shared/styles.scss' ],
  changeDetection: ChangeDetectionStrategy.OnPush,
  standalone: true,
  imports: [FormModule],
})
export class ForgotPasswordComponent implements OnInit {

  formGroup: FormGroup<ForgotPasswordForm>;

  constructor() { }

  ngOnInit() {
    this.createForm();
  }

  private createForm(){
    this.formGroup = new FormGroup<ForgotPasswordForm>({
      email: new FormControl('your@gmail.com', {
        nonNullable: true,
        validators: [RxwebValidators.required(),
        RxwebValidators.email()]
      })
    })
  }

  forgotPassword(){
    let credential: ForgotPassword = this.formGroup.getRawValue();
    console.log(credential);
  }

}
