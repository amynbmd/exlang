import { ChangeDetectionStrategy, Component, OnInit } from '@angular/core';
import {MatCardModule} from '@angular/material/card';
import {MatDividerModule} from '@angular/material/divider';
import {MatIconModule} from '@angular/material/icon';

@Component({
  selector: 'app-past',
  templateUrl: './past.component.html',
  styleUrls: ['./past.component.css'],
  changeDetection: ChangeDetectionStrategy.OnPush,
  standalone: true,

  imports: [
    MatCardModule, MatDividerModule, MatIconModule,
  ]
})
export class PastComponent implements OnInit {

  constructor() { }

  ngOnInit() {
  }

}
