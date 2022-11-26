import { CommonModule } from '@angular/common';
import { ChangeDetectionStrategy, Component, Input, OnInit } from '@angular/core';
import { MatButtonModule } from '@angular/material/button';
import { MatCardModule } from '@angular/material/card';
import { MatIconModule } from '@angular/material/icon';
import { Observable } from 'rxjs';
import { User } from 'src/app/account/_models/user';
import { SelectItem } from 'src/app/_models/select-item';

@Component({
  selector: 'app-user-card',
  templateUrl: './user-card.component.html',
  styleUrls: ['./user-card.component.css'],

  changeDetection: ChangeDetectionStrategy.OnPush,
  standalone: true,
  imports: [
    CommonModule,
    MatCardModule,
    MatButtonModule,
    MatIconModule
  ]
})
export class UserCardComponent implements OnInit {
  @Input() user: User;
  @Input() languages$: Observable<SelectItem[]>;
  
  //Generate random image of fake people
  //https://this-person-does-not-exist.com/en

  constructor() { }

  ngOnInit() {
  }

  getSelectItemName(list: SelectItem[], code: string) {
    return list.filter(m => m.code == code)[0]?.name;
  }
}
