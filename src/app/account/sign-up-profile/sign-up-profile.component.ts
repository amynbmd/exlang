import { ChangeDetectionStrategy, ChangeDetectorRef, Component, OnInit } from '@angular/core';
import { FormControl, FormGroup } from '@angular/forms';
import { MatSelectModule } from '@angular/material/select';
import { Router, RouterModule } from '@angular/router';
import { RxwebValidators } from '@rxweb/reactive-form-validators';
import { Observable } from 'rxjs';
import { SelectItem } from 'src/app/_models/select-item';
import { FormModule } from 'src/app/_modules/form.module';
import { BaseComponent } from 'src/app/_shared/BaseComponent';
import { SignUpProfile } from '../_models/sign-up-profile';
import { SignUpProfileForm } from '../_models/sign-up-profile.form';
import { AuthenticationService } from '../_services/authentication/authentication.service';

@Component({
  selector: 'app-sign-up-profile',
  templateUrl: './sign-up-profile.component.html',
  styleUrls: ['./sign-up-profile.component.scss', '../_shared/styles.scss'],
  changeDetection: ChangeDetectionStrategy.OnPush,
  standalone: true,
  imports: [
    RouterModule, FormModule, MatSelectModule
  ]
})
export class SignUpProfileComponent extends BaseComponent implements OnInit {
  formGroup: FormGroup<SignUpProfileForm>;
  countries$: Observable<SelectItem[]>;
  languages$: Observable<SelectItem[]>;
  levels$: Observable<SelectItem[]>;

  constructor(
    private _authService: AuthenticationService, 
    private _router: Router,
    private _cd: ChangeDetectorRef) { super(); }

  ngOnInit() {
    this.createForm();
    this.countries$ = this._authService.getCountries();
    this.languages$ = this._authService.getLanguages();
    this.levels$ = this._authService.getLevels();
  }

  submit() {
    let profile: SignUpProfile = this.formGroup.getRawValue();
    this.summaryError = [];

    this._authService.updateUserProfile(profile).subscribe(response => {
      this._router.navigate(['user-profile-area']);
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


  private createForm() {
    const user = this._authService.getUserFromLocalStorage();

    this.formGroup = new FormGroup<SignUpProfileForm>({
      email: new FormControl(user.email, {
        nonNullable: true,
        validators: [RxwebValidators.email(), RxwebValidators.required()],
      }),      
      countryCode: new FormControl('', {
        nonNullable: true,
        validators: [RxwebValidators.required()],
      }),
      nativeLang: new FormControl('', {
        nonNullable: true,
        validators: [RxwebValidators.required()],
      }),
      learningLangs: new FormControl([], {
        nonNullable: true,
        validators: [RxwebValidators.required()],
      }),
      level: new FormControl('', {
        nonNullable: true,
        validators: [RxwebValidators.required()],
      }),
      interest: new FormControl('', {
        nonNullable: true,
        validators: [RxwebValidators.required()],
      })
    });
  }
}
