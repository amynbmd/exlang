import { CommonModule } from '@angular/common';
import { ChangeDetectionStrategy, Component, OnInit } from '@angular/core';
import { MatButtonModule } from '@angular/material/button';
import {MatChipsModule} from '@angular/material/chips';
import {MatDividerModule} from '@angular/material/divider';
import { Router } from '@angular/router';
import { Observable } from 'rxjs';
import { User } from 'src/app/account/_models/user';
import { AuthenticationService } from 'src/app/account/_services/authentication/authentication.service';
import { SelectItem } from 'src/app/_models/select-item';

@Component({
  selector: 'app-user-bio',
  templateUrl: './user-bio.component.html',
  styleUrls: ['./user-bio.component.css'],
  changeDetection: ChangeDetectionStrategy.OnPush,
  standalone: true,

  imports: [
    CommonModule,
    MatButtonModule, MatChipsModule, MatDividerModule
  ]
})
export class UserBioComponent implements OnInit {

  user$: Observable<User>;
  countries$: Observable<SelectItem[]>;
  languages$: Observable<SelectItem[]>;

  constructor(private _authService: AuthenticationService, private _router: Router) { }

  ngOnInit() {
    let user = this._authService.getUserFromLocalStorage();
    if (user.email != null) {
      this.user$ = this._authService.getUserProfile(user.email);
      this.countries$ = this._authService.getCountries();
      this.languages$ = this._authService.getLanguages();

  
    } else {
      this._authService.logout();
      this._router.navigate(['account', 'area']);
    }
  }


  getSelectItemName(list: SelectItem[], code: string) {
    return list.filter(m => m.code == code)[0].name;
  }
}
