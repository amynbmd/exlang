import { CommonModule } from '@angular/common';
import { ChangeDetectionStrategy, ChangeDetectorRef, Component, OnInit } from '@angular/core';
import { FormControl, FormGroup } from '@angular/forms';
import { MatButtonModule } from '@angular/material/button';
import {MatChipsModule} from '@angular/material/chips';
import {MatDividerModule} from '@angular/material/divider';
import { MatSelectModule } from '@angular/material/select';
import { Router } from '@angular/router';
import { RxwebValidators } from '@rxweb/reactive-form-validators';
import { Observable } from 'rxjs';
import { SignUpProfile } from 'src/app/account/_models/sign-up-profile';
import { SignUpProfileForm } from 'src/app/account/_models/sign-up-profile.form';
import { User } from 'src/app/account/_models/user';
import { AuthenticationService } from 'src/app/account/_services/authentication/authentication.service';
import { SelectItem } from 'src/app/_models/select-item';
import { FormModule } from 'src/app/_modules/form.module';
import { BaseComponent } from 'src/app/_shared/BaseComponent';

@Component({
  selector: 'app-user-bio',
  templateUrl: './user-bio.component.html',
  styleUrls: ['./user-bio.component.css'],
  changeDetection: ChangeDetectionStrategy.OnPush,
  standalone: true,

  imports: [
    CommonModule,
    MatButtonModule, MatChipsModule, MatDividerModule, FormModule, MatSelectModule
  ]
})
export class UserBioComponent extends BaseComponent  implements OnInit {
  formGroup: FormGroup<SignUpProfileForm>;
  user$: Observable<User>;
  countries$: Observable<SelectItem[]>;
  languages$: Observable<SelectItem[]>;
  levels$: Observable<SelectItem[]>;

  editMode: boolean = false;

  constructor(private _authService: AuthenticationService, private _router: Router, private _cd: ChangeDetectorRef) { super() }

  ngOnInit() {
    let user = this._authService.getUserFromLocalStorage();
    if (user.email != null) {
      this.user$ = this._authService.getUserProfile(user.email);
      this.countries$ = this._authService.getCountries();
      this.languages$ = this._authService.getLanguages();
      this.levels$ = this._authService.getLevels();

      this.createForm();
      this.patchForm();
  
    } else {
      this._authService.logout();
      this._router.navigate(['account', 'area']);
    }
  }


  getSelectItemName(list: SelectItem[], code: string) {
    return list.filter(m => m.code == code)[0]?.name;
  }

  changeMode() {
    this.editMode = !this.editMode;
  }

  submit() {
    let profile: SignUpProfile = this.formGroup.getRawValue();
    this.summaryError = [];

    console.log(profile);

    this._authService.updateUserProfile(profile).subscribe(response => {
      this.editMode = false;
      if (response.email != null) {
        this.user$ = this._authService.getUserProfile(response.email);
        this.patchForm();
      }
      


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
      }),
      bio: new FormControl('', {
        nonNullable: true,
        validators: [],
      })
    });
  }

  private patchForm() {
    this.user$.subscribe(response => {
      if (!this._authService.userHasProfile(response.profile)) {
        this._router.navigate(['account', 'area'], { queryParams: {completeProfile: false}})
        .then(() => {
          window.location.reload();
        });;

      }


      const profile: SignUpProfile = {
        email: response.email,
        countryCode: response.profile.countryCode,
        nativeLang: response.profile.nativeLang,
        learningLangs: response.profile.learningLang,
        level: response.profile.level,
        interest: response?.profile?.interests?.join(", "),
        bio: response.profile.bio,    
      };

      this.formGroup.patchValue(profile);
    });
  }
}
